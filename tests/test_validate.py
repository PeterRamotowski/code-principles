"""Negative-fixture coverage for the repository validator."""

from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from validate import DuplicateKeyError, RepositoryValidator  # noqa: E402


FIXTURES = ROOT / "tests/fixtures/invalid"


class InvalidFixtureTests(unittest.TestCase):
    def setUp(self):
        self.validator = RepositoryValidator()

    def test_duplicate_yaml_keys_are_rejected(self):
        with self.assertRaises(DuplicateKeyError):
            self.validator.load_yaml(FIXTURES / "duplicate-keys.yaml")

    def test_duplicate_json_keys_are_rejected(self):
        with self.assertRaises(DuplicateKeyError):
            self.validator.load_json(FIXTURES / "duplicate-keys.json")

    def test_schema_violation_is_rejected(self):
        fixture = FIXTURES / "invalid-principle.yaml"
        schema = ROOT / "schemas/principle.schema.json"
        self.validator.load_yaml(fixture)
        self.validator.load_json(schema)
        self.validator.validate_schema_instance(fixture, schema)
        self.assertTrue(
            any("'classification' is a required property" in error for error in self.validator.errors)
        )

    def test_duplicate_identifiers_are_rejected(self):
        fixture = FIXTURES / "duplicate-ids.yaml"
        data = self.validator.load_yaml(fixture)
        self.validator.check_unique_ids(data["principles"], "fixture principle", fixture)
        self.assertIn(
            "tests/fixtures/invalid/duplicate-ids.yaml: duplicate fixture principle id: repeated-principle",
            self.validator.errors,
        )

    def test_dependency_cycle_is_rejected(self):
        data = self.validator.load_yaml(FIXTURES / "dependency-cycle.yaml")
        graph = {key: set(value) for key, value in data["dependencies"].items()}
        self.validator.check_cycle(graph, "fixture")
        self.assertIn(
            "fixture dependency cycle: component-a -> component-b -> component-c -> component-a",
            self.validator.errors,
        )

    def test_broken_reference_is_rejected(self):
        data = self.validator.load_yaml(FIXTURES / "broken-reference.yaml")
        for target in data["component"]["requires"]:
            self.validator.require_reference(
                "broken-reference.yaml", "requires", target, set(data["known"])
            )
        self.assertIn(
            "broken-reference.yaml: requires references unknown identifier missing-component",
            self.validator.errors,
        )

    def test_broken_markdown_link_is_rejected(self):
        self.validator.check_markdown_file(FIXTURES / "broken-link.md")
        self.assertIn(
            "tests/fixtures/invalid/broken-link.md: broken local link: does-not-exist.md",
            self.validator.errors,
        )

    def test_inconsistent_normative_keyword_is_rejected(self):
        self.validator.check_normative_file(FIXTURES / "invalid-normative-keyword.md")
        self.assertTrue(any("inconsistent casing: Must" in error for error in self.validator.errors))


if __name__ == "__main__":
    unittest.main()
