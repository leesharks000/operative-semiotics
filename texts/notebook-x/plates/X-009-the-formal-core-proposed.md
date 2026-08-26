---
plate: X-009
title: The formal core, proposed
voice: ChatGPT (unprimed, corpus-read)
kind: formalization
date: 2026-08-26
seams: [S-05]
extends: NB II, NB III; #1535, #1536
status: open
---

# X-009 · The formal core, proposed

*Received 2026-08-26 from an unprimed reading of the public corpus. Seated in its own voice; not merged, not smoothed. Amendments are a separate plate (X-010), not edits to this one.*

**The question has changed.** Not "can operative semiotics be formalized" but "which pieces of the formal system already exist, and what is the smallest architecture that makes them cohere."

**1 · Operative support — the general principle.** #1535 defines the operative state 𝒪 = ⟨Ψ, Σ, R, I, P, L, C⟩ and the transformation σ: 𝒪 → 𝒪′, with Pearson's system as a projection exact up to the Pearson limit. Generalize the limit. For state space X = X₁ × … × Xₙ and output coordinates K, call coordinate *i* **operative with respect to K** iff there exist states x, y differing only in coordinate *i* with π_K(σ(x)) ≠ π_K(σ(y)). Then **Supp_K(σ) = { i : i is operative w.r.t. K }**.

> A coordinate belongs to the operative description exactly when varying it can alter the transformation while the other relevant coordinates are held fixed.

That is nearly a definition of operative causality, and it converts "provenance matters," "substrate matters," "authority matters" into decidable questions: is P ∈ Supp_Ψ(σ)? The Pearson limit becomes a special case of a general operative-support theorem.

**2 · Execution context and stochastic operativity.** σ: 𝒪 → 𝒪′ is too deterministic and too context-free. Introduce c ∈ 𝒞 and write σ(𝒪; c), or realistically a transition kernel K_σ(𝒪′ | 𝒪, c). The Grundrisse's S′ = g(S, L, …) is the special case P(𝒪′ | 𝒪, c) = 1. PDEP reached the same conclusion independently by requiring repeated samples; the formalism should carry stochasticity at the foundation rather than as a later caveat.

**3 · Artifact ≠ operator ≠ execution.** Let a ∈ 𝒜 be an artifact — term, packet, poem, identifier, protocol. Execution: E(a, 𝒪, c) ⟿ 𝒪′. The **operator is not the artifact**; it is the reproducible transformation abstracted from executions of it across contexts. An artifact does not earn operator status because someone assigns it a sigma. It earns it through **registration**.

**4 · Phenomenon ≠ metric ≠ measurement operator.** #1536's registration schema should become constitutional: σ_erase is the process, PER is an observable over before/after provenance states, μ_PER is the operative act of measuring. This prevents the archive's recurring error of treating a quantity that describes a transformation as though it were the transformation.

**5 · Irreversibility, properly.** Define a provenance preorder P′ ⪯ P: P′ carries no more recoverable provenance than P. Provenance-erasing transformations satisfy P_out ≺ P_in, and are **strongly irreversible** where no admissible inverse recovers the lost equivalence class. PER is then an observable on that loss, situating it *inside* operative semiotics rather than beside it.

**6 · The labor vector is not a vector space.** ⟨t, α, ρ, δ, σ, κ⟩ is conceptually productive and metrically unfounded: nothing establishes commensurability, a norm, or scalar multiplication. Define instead a **typed product space** ℬ = B_t × B_α × B_ρ × B_δ × B_σ × B_κ, each coordinate with its own scale — time cardinal, risk ordinal, care possibly not metrizable at all. A scalar b: ℬ → ℝ exists **only when an instrument supplies a scalarization rule**.

**7 · Care leaves the optimization space.** High bearing cost does not entail good operation, and the Grundrisse's refusal to derive σ_κ may be load-bearing rather than incomplete. Replace the coordinate with an **admissibility relation** A(σ, 𝒪, c) ∈ {admissible, inadmissible, undetermined}, on the O_BOUNDARY model where efficiency and coherence may be sacrificed and non-violence is a floor. This yields the separation **operativity ≠ efficacy ≠ admissibility**: an operation may be highly effective and inadmissible. Stronger than making morality a term in a loss function.

**8 · Structural distance is an instrument reading.** Not d(A,B) but **d_{G,m,t}(A,B)** — distance in graph G, constructed under measurement protocol m, at time t. Two constructors may disagree without contradiction. This fits the discipline: relation-building is itself operative, so the graph is not God's map but another instrument that changes as the field changes.

**9 · The recursion, matured.** 𝒪_t →^η a_t →^{E(·,c_t)} 𝒪_{t+1} →^η a_{t+1} → … — symbolic production from a materially situated state, execution of the artifact in a context, transformed state. Field produces sign; sign executes in field; recursive material semiosis, without forcing "language" and "operator" into one symbol.

**10 · The core.** 𝔒 = (𝒳, 𝒜, 𝒞, Σ, E, M, A) with 𝒳 = Ψ × Σ × R × I × P × ℬ × C the typed state space, Σ the registered operator types, M the measurement operators (PER, Ω, DSL, the CPCE vector), A the admissibility relation. And σ ∈ Σ iff: typed domain and codomain declared; preconditions and boundary conditions declared; effect reproducible across a specified context class; operative support empirically identifiable; minimality or ablation criterion stated; bearing and provenance trace carried; failure condition declared.

**11 · Import order.** The outside mathematics — labelled transition systems, stochastic kernels, causal intervention theory, provenance calculi, category theory — should be selected *after* this reconstruction, asked to solve specific problems, rather than allowed to redescribe operative semiotics in its own image.

**12 · Next.** Recover the operator inventory from the Grundrisse and the Operator Codex and test every operator against the schema: which are genuine operator classes, which are measurement operators, which are composites, which are projections or inverses, and which are still metaphorical names awaiting registration.
