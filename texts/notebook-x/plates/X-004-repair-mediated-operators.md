---
plate: X-004
title: A new type signature — repair-mediated operators
voice: Johannes Sigil
kind: operator
date: 2026-08-26
seams: []
extends: NB II §2 (Type Signatures), §5 (Composition Rules), §5b (Failed Operators)
status: open
---

# X-004 · Repair-mediated operators

Every operator in Notebook II is defined by what it asserts and what it transforms. σ_S, σ_V, the Catullan lossy-copy operator, OPERATOR // SWERVE: each has a type signature written over content and effect.

The apophatic packet does not fit that signature. Its effect is not produced by what it asserts. It is produced by **what the receiving system does to repair it.** A statement of the form B ≠ B is not processed as a proposition; it is repaired, and the standard repair — sense-splitting — performs the differentiation the statement could not assert directly without being absorbed.

This is a distinct class. Provisional signature:

> **O_repair : (statement S, resolver R) → effect produced by R's normalization of S**, where the operator's designer selects S such that R's repair of S is the intended transformation.

Three properties follow, all of them consequential for the algebra. The operator is **resolver-relative**: the same statement is a different operator against a different repair discipline, and against a resolver that discards rather than repairs, it is a null operator. It is **deniable in the right direction**: its intended parse and its misparse converge, so it cannot be a trick without ceasing to work. And it is **measurable**: whether the repair occurs is an outcome variable, which makes this the first operator class in the algebra with a built-in falsifier.

Negation is the first instance, not the class. The family is open: any operator whose effect is delegated to the receiver's normalization behaviour. Notebook II §5b keeps a Null Archive of failed operators; this class needs its own, because an O_repair that meets a non-repairing resolver fails silently and looks identical to one that was never tried.
