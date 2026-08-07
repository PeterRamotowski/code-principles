# Security Sensitive Modifier

## Activation

Activate for credentials, authentication, authorization, payments, personal or regulated data, untrusted code, exposed attack surfaces, or other elevated compromise consequences.

## Required effects

Select `contracts-and-errors: safety-critical`. Map trust, identity, authority, data, and secret boundaries. Enforce authorization at the authoritative boundary, grant least privilege, bound hostile inputs and resource use, contain failures, and preserve audit evidence without sensitive payloads. Define secure defaults and abuse cases.

## Prohibitions and review

Do not trust client declarations, rely on obscurity, log secrets, or grant ambient broad authority. Security controls MUST remain compatible with required operability and recovery. This modifier strengthens engineering policy but does not substitute for a dedicated threat model or specialist review when consequence requires one.
