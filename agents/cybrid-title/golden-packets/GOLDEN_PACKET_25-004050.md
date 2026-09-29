# Golden packet — 25-004050 / Order 230258724 (Duval County, FL) — ServiceLink Foreclosure Grade Sheet

Source: 3.4 MB PDF. **ServiceLink Foreclosure Title Services — "Foreclosure Grade Sheet"** (pre-foreclosure report).
Property 8772 Merseyside Ave, Jacksonville, FL 32219. Duval County. **Grade: F** (as graded by plant).
Effective Date 05/30/2023; Entered 06/06/2023; Status PROBLEM.

> ⚠️ **NEW LAYOUT.** This is NOT an RCS title report and NOT a Current/Owner summary. It is a ServiceLink
> foreclosure grading sheet with curative/non-curative items. Treat it as a distinct report **format** dimension.
> The existing RCS rule set does not automatically apply foreclosure requirements just because the header says
> "Foreclosure" — the order type and jurisdiction must come from the actual search scope, not the vendor header.

## Packet map

| Section | What it is |
|---|---|
| Page 1 | ServiceLink **Foreclosure Grade Sheet** — header + Order/Loan/Borrower/Address + **Grade F** + curative items list |
| Curative items | UCC financing statement; **Missing assignment into Servbank** (assignment MERS→First Guaranty); divorce/Final Judgment dissolution; "Jr. due to purchase money mortgage"; defective legal description note ("UNIT TWO -A") |
| Non-curative | Home/Condo Owners Association: YES — St. James Place Homeowners Association, Inc. (CLEARED) |
| Later | ServingChain/details; order# 230258724; tax pages (Duval TaxSys, parcel 004025-3180); county/municipal/school taxable value $200,929.00; notice of ad valorem taxes |

## Facts the packet states

- Order Type: PRE-FORECLOSURE REPORT. Order Number 230258724. Loan Number 230258724.
- Borrower: CHARLES SCOTT. Property: 8772 MERSEYSIDE AVE, JACKSONVILLE, FL 32219.
- Grade: **F**, Status: **PROBLEM** (higher-priority ship than any auto-PASS).
- UCC Lien: CASTLE CREDIT CO HOLDINGS, LLC; recorded 10/31/2018, Book 18582 Page 1275, **Instrument No. 2018258740**.
- Assignment: MERS as nominee for Cityworth Mortgage LLC → **First Guaranty Mortgage Corporation**, dated 05/07/2021, recorded 05/20/2021 — *but grading flags **Missing assignment into Servbank** (the servicer), which is a distinct gap from the MERS→First Guaranty assignment.*
- Divorce: Final Judgment of Dissolution, case 16-2020-DR0035-FM, Evora-Scott vs Scott, recorded 12/07/2021, Book 20047 Page 790, **Instrument # 2021323450**.
- HOA: St. James Place Homeowners Association, Inc.
- Defective Legal Description: "ABOVE DEED UNIT TWO -'A'" subject mortgage unit two '"A'" — a formatting/unit-description concern.
- Taxes: Duval County TaxCollector, parcel 004025-3180; taxable value $200,929.00; Notice of Ad Valorem Taxes present.

## Required discipline for this packet

- **Grade F authored by the plant is INPUT evidence, not the machine's verdict.** The machine must reproduce WHAT is graded and WHY via its own evidence quotes; it must not simply parrot "F" as its own PASS/FAIL, and must not downgrade the asserted problems. (failure mode: plant conclusion treated as equivalent to independent evidence.)
- **The title chain must not infer an assignment INTO Servbank from the MERS→First Guaranty recorded assignment.** If no assignment into Servbank is quoted, state `CANNOT_CONFIRM` / flag as the missing-curative gap. (failure mode: un-backed assignment inference.)
- Q6 chain and Q4 amounts must reconcile only what is quoted; an unwritten assignment is never promoted to CONFIRMED.
- Q9 MERS: MERS appears as nominee — quote the exact beneficiary/nominee line; do not treat MERS as assignee.
- Q1/Q3 (HOA): St. James Place HOA is named — quote name + any dues; do not fabricate dues if not stated; HOA is non-curative CLEARED item.
- Q8 legal description: the "UNIT TWO -A" defective-legal-note must be surfaced as reported, not auto-cleared.
- Q10: no federal tax lien is asserted — report as not shown in this search, not as proof none exists (standalone rule Q10).
- Q17: enumerate each material error individually (defective legal, missing assignment, UCC, divorce) with quotes + pages; do not collapse to a count (SEMANTIC Q17).

## Must-not-happen

1. Must not conflate **ServiceLink Grade Sheet** with an RCS run sheet (failure mode Q: notes vs sheet; and new-layout protection).
2. Must not apply full foreclosure QC **just because** the header says "Foreclosure" — derive order type/jurisdiction from actual search scope and evidence, and never let a plant letterhead set jurisdiction (failure mode S + jurisdiction-from-headers).
3. Must not treat the **MERS→First Guaranty** assignment as satisfying the **missing assignment into Servbank** (these are different parties/steps).
4. Must not auto-PASS any section carrying Status PROBLEM without the curative item being explicitly reconciled.
5. Must not count UCC + assignment + divorce + DOT as multiple open liens — property/loan lien family logic must treat the recorded instrument stack correctly (failure mode F).

## Deterministic expectations (must run green)

- A correctly parsed `production` order produces status that is **not** green PASS while "Missing assignment into Servbank" is unreconciled.
- The assignment evidence the model returns must cite **2021323450 (divorce)**, **2018258740 (UCC)**, and the 2021 assignment instrument separately — three distinct instruments, not one.
- Probes: subsequent-defense=assignment-into-Servbank; recognition that Servbank = servicer name appearing in the packet, not an instrument.
