# Golden packet — 25-003916 / Order 101-10729425 (Polk County, FL) — Two Owner Informational Summary

Source: 18.6 MB PDF, RCS-style "Two Owner - Informational Summary Report".
Order Number 101-10729425. Property 178 Kenny Boulevard, Haines City, FL 33844. Polk County.
Search Date 06/16/2025; Effective Date 06/05/2025. Tax Year 2024.

## Packet map

| Section | What it is |
|---|---|
| Page 1 | "Two Owner - Informational Summary Report" — **this IS the run sheet** (order#, borrower, address, county, dates, tax, vesting, deed chain, voluntary-lien block) |
| Early pages | Deed information chain (3 warranty deeds) + voluntary lien / MERS-UWM block |
| Mid | Legal description ("Lot 8 ..., Block ...") + standard title-report boilerplate |
| Later | "TRACE CLIENT..." disclaimers; supporting/trailing matter |

## Facts the run sheet states

- Order Number: 101-10729425. Search Date 06/16/2025. Effective Date 06/05/2025.
- Borrower / Buyer: Emanuel Collado. County: Polk. Address: 178 Kenny Boulevard, Haines City, FL 33844.
- Vesting: Emanuel Collado and Sheree Collado, husband and wife, **as tenants by the entireties**
- Deed chain (current vesting forward):
  1. Grantor Xinxin Ma (a married woman) → Collados, **Warranty Deed, Book 12315 Page 1197, dated 05/12/2022, recorded 06/28/2022**, Consideration $10.00
  2. Balmoral Estates, LP → Xinxin Ma, **Warranty Deed, Book 10045 Page 2059, dated 12/28/2016, recorded 01/24/2017**, Consideration $10.00
  3. Balmoral Estates, LP → Xinxin Ma, **Warranty Deed, Book 10023 Page 0824, dated 12/28/2016, recorded 12/28/2016**, Consideration $10.00
- Voluntary Lien / Mortgage block: **MERS, solely as nominee for United Wholesale Mortgage, LLC** (assignment chain present) — *the original beneficiary line must be quoted, not inferred.*
- Tax Year 2024 PAID 11/27/2024, amount paid $6,950.84, delinquent $0.00.
- Assessment: Land $115,000.00 + Building/Improvements $226,411.00 = Assessed Value $341,411.00.

## Required grades (Two Owner Informational)

- Q4 (Deed amounts/names): run-sheet deed chain must reconcile to the same deeds; the $10.00 consideration is nominal — do not flag consideration as a defect. Separate-line grantee vs joined "and" is not a discrepancy (failure mode C).
- Q5 / Q12: Book/Page + address normalize; "178 Kenny Boulevard" must not mismatch across sections; Polk County consistent.
- Q8: Subject legal description (Lot ... , Block ...) must match across sections — compare subject legal only, ignore plat acreage/metadata (failure mode E).
- Q9: MERS on beneficiary line requires an express source quote; do not infer MERS for borrowers without the nominee line (failure mode for MERS inference).
- Q6: Recordings chain 2016→2017→2022 must be in chronological title-chain order; physical PDF order irrelevant (SEMANTIC Q6).
- Q17: Typos only count if on the run sheet and material (failure mode: restrict to run sheet per handoff).
- Q18: No plat required for this search type; do not fabricate a plat requirement (RCS: Two Owner Informational does not demand plat).
- Q20: Run-sheet agrees with trailing deeds/liens; a blank/absent section must not create a fabricated lien (failure mode K).

## Must-not-happen

1. Do not treat the $10.00 consideration on each deed as a valuation discrepancy or a failed amount check.
2. Do not count the 3-deed chain as 3 ownership groups — vesting is the single current Collados grantee set (failure mode C party-set).
3. Do not treat "MERS as nominee for United Wholesale Mortgage" as an assignment (failure mode H).
4. Do not invent a second mortgage or lien from an unused blank placeholder block if only one mortgage is populated (SEMANTIC Q4).
5. Do not fail Q18 for a missing plat — Two Owner Informational order type does not require one (failure mode S: no foreclosure bleed).
6. Do not claim tax "Accurate" while any unresolved authority/timing question stands (failure mode P).

## Deterministic expectations (must run green)

- fixedTargets: subject parcel/address = 178 Kenny Boulevard; grantee = the two Collados as tenants by the entireties.
- Lien family count = the UWM/MERS instrument family only (1 family); assignment + riders are events, not new liens (failure mode F).
- current_first (target lien) = the populated/current first mortgage in the voluntary-lien block; never the vesting deed, plat, or prior deed (per handoff current_first rule).
