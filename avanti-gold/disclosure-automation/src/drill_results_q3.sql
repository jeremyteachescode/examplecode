-- Avanti Gold Corp. (AVNT) Q3 2026 drill program: composite assay results by hole
-- Feeds the technical summary referenced in the Form 5 MD&A.
SELECT
    h.hole_id,
    h.target_zone,
    SUM(a.interval_m)                                  AS total_interval_m,
    ROUND(SUM(a.au_gpt * a.interval_m) / SUM(a.interval_m), 2) AS weighted_au_gpt,
    MAX(a.au_gpt)                                      AS peak_au_gpt
FROM drill_holes h
JOIN assay_intervals a ON a.hole_id = h.hole_id
WHERE h.project = 'Avanti Gold - Phase 1'
  AND h.completed_date BETWEEN '2026-07-01' AND '2026-09-30'
  AND a.qa_qc_status = 'APPROVED'
GROUP BY h.hole_id, h.target_zone
HAVING weighted_au_gpt >= 1.0
ORDER BY weighted_au_gpt DESC;
