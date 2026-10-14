# Related work and project positioning

Review date: **2026-10-14**. Project status: **planning; implementation and benchmarks pending**.

This document accompanies [the project README](../README.md) and [the implementation plan](../CODEX_PROJECT_START.md). It records relevant prior work, the proposed scope of this project, and the evidence needed to support future claims.

## Scope and limits of this review

The review covers publicly accessible repository descriptions, READMEs, and project documentation found through targeted searches for LANL authentication anomaly detection, temporal graph lateral movement detection, and community-aware graph anomaly detection. Search terms included combinations of `LANL`, `authentication`, `Louvain`, `Leiden`, `community detection`, and `lateral movement`.

The referenced implementations were **not executed or comprehensively audited**. Their performance claims have not been independently reproduced. Repository links identify the accessible copies reviewed; a README describing a repository as official is not independent verification of its provenance. Before reproducing or importing code, verify the upstream source and record a commit SHA.

No reviewed source was established to implement the complete experiment and systems contract proposed here. This is a limited search finding, **not proof of uniqueness**. An unmentioned capability must be treated as unknown, rather than absent.

## Relevant projects

| Work | Documented approach | Relationship to this project | Difference in proposed scope |
|---|---|---|---|
| [Jbeil][R1] | Temporal graph representations and inductive link prediction for lateral movement; includes LANL authentication data. | Closely related problem, data source, and temporal graph setting. | We plan explicit community features and simple baseline models, with controlled quality/resource experiments. |
| [LANL Auth Redteam][R2] | Authentication anomaly pipeline describing Isolation Forest, One-Class SVM, Local Outlier Factor, and LSTM. | Same auth/redteam files and overlapping classical anomaly models. | We focus on community feature ablations and a specified causal replay protocol. |
| [Lateral Movement Graph Detection][R3] | Directed user/device graph, frequency baselines, time-window subgraphs, and suspicious multi-hop paths; synthetic demo. | Related graph construction, temporal windows, and alert generation. | Our primary comparison is event scoring with Louvain/Leiden features, rather than multi-hop path scoring. |
| [ComGA][R4] | Community-aware attributed graph anomaly detection using a modularity-matrix autoencoder and tailored graph convolutional network. | Establishes that community information for graph anomaly detection is prior work. | Our proposed LANL event-stream experiment uses windowed community features and classical models; ComGA documents attributed-node tasks and datasets such as BlogCatalog, ACM, and Flickr. |
| [Security Anomaly Detection][R5] | CICIDS2017 flow replay with Kafka, rolling features, statistical/Isolation Forest/LSTM approaches, and drift checks. | Related ML pipeline and replay engineering concerns. | Our data are identity/authentication events; V1 is a single-machine worker with graph snapshots and no Kafka requirement. |
| [Seerflow graph detection documentation][R6] | Louvain communities and community-crossing alerts within a broader graph detection system. | Direct precedent for using community boundaries as a lateral movement signal. | We propose controlled LANL evaluation of community features, refresh frequency, and measured processing costs. The reviewed page does not establish an equivalent benchmark. |

These differences describe this project's intended scope. They are not claims that the referenced systems lack testing, scalability, or production capabilities.

## What is already established

Authentication anomaly detection on LANL, temporal graph approaches to lateral movement, community-aware graph anomaly detection, and Louvain community-crossing signals all have relevant precedents [R1–R6]. None should be presented as an invention of this project.

The Louvain and Leiden algorithms are existing methods [R7, R8]. Using Leiden instead of Louvain does not by itself establish a new scientific contribution. Isolation Forest and temporal feature engineering are also components to evaluate, rather than novel algorithms claimed here.

## Intended contribution

The project aims to provide a reproducible ML systems implementation and an empirical study of this question:

> Under measured CPU and memory constraints, how do community features, graph refresh frequency, and snapshot availability affect known-positive detection, scoring latency, and resource consumption on authentication event streams?

This is a proposed engineering contribution. Its usefulness must be demonstrated by implementation, tests, and measurements; none are complete at the time of this document.

| Proposed evidence | Experiment or test | Required reporting |
|---|---|---|
| Incremental value of graph/community features | B0 rule; B1 temporal features + Isolation Forest; B2 adds graph features; B3/B4 add Louvain/Leiden features. | Common split, eligible events, alert grouping, budgets, and label coverage. |
| Freshness versus processing cost | Compare 15-minute, 1-hour, and 4-hour refresh schedules with a fixed graph window. | Known-positive recall/yield, snapshot age, compute time, total CPU, peak memory, backlog, and latency. |
| Causal feature correctness | Future invariance, same-second permutation, batch-boundary invariance, and offline/replay parity. | Test fixtures and actual test outcomes. |
| Recovery correctness | Crash and resume at defined checkpoint boundaries. | Logical output and state equivalence; no duplicate state updates. |
| Performance improvement | Profile a concrete bottleneck and change one implementation decision. | Before/after results on the same workload, hardware, versions, and configuration. |

### Controls for the refresh experiment

1. Run the small B0–B4 comparison before expanding the experiment matrix.
2. For each refresh-policy configuration, generate causal training features and fit its model using only its training split. Fix the other model hyperparameters; choose any settings using validation only. Report each configuration's model version.
3. Run a separate frozen-model stress experiment only if evaluating delayed or stale snapshots at deployment. Label it explicitly: it measures deployment mismatch and cannot be pooled with the matched-training comparison.
4. Keep graph window, weight transform, alarm grouping, data split, eligible population, and resource settings fixed when isolating refresh frequency. Report the actual schedule and snapshot age, not only the requested interval.
5. Separate deterministic causal replay from operational asynchronous replay. Include snapshot computation and publication delays in the operational measurements.
6. If a configuration cannot sustain input rate, report backlog growth or failure. Do not silently reduce the input or exclude difficult events.

An experiment that finds no useful benefit from community features is still informative. Report the observed tradeoff and avoid selecting only favorable runs.

## Evaluation compatibility

Results in the referenced repositories must not be placed beside our numbers as if they were directly comparable. A meaningful numerical comparison requires compatible data versions, event filtering, labels, train/validation/test periods, alarm units, and metric definitions.

In particular, known red-team labels do not establish that all other LANL events are benign [R9]. This project will distinguish known-positive recall/yield from ordinary precision claims. Daily retrospective top-B ranking and online thresholded alerts are separate evaluations.

Our B0–B4 ablation is the first required comparison. Reproducing Jbeil, ComGA, or another external system is optional later work with a separate reproducibility assessment. Their installation or unavailable artifacts must not block the initial synthetic demo.

## Attribution and code reuse

**Current record:** These documents cite prior work. No source code from the listed repositories has been imported as part of preparing this documentation. No external implementation has been reproduced by this project yet.

For each future dependency or reused component:

1. Identify its upstream repository and immutable commit or release.
2. Inspect the applicable license for the exact files and version.
3. Preserve required notices and record modifications.
4. Attribute conceptual inspiration separately from copied/adapted code.
5. Record reproduction attempts separately from original experiments.

Public visibility is not a blanket reuse license. GitHub explains that repositories without a license retain default copyright restrictions; citing a repository does not substitute for permission [R10].

Maintain this record when reuse actually occurs:

| Component/path in this project | Upstream and commit/version | Relationship | License/notice obligations | Changes and verification |
|---|---|---|---|---|
| No imported component recorded at documentation stage | Not applicable | Documentation references only | Check before reuse | No implementation assessed |

Use relationship values such as `dependency`, `adapted code`, `independent implementation of a published method`, or `experiment reproduction`. Do not describe an adapted implementation as entirely original.

## Claim policy

Appropriate now: “A planned reproducible ML systems study of community features for authentication anomaly detection.”

Appropriate after verification: a precise statement of the implemented capability or measured result, including dataset scope, hardware, configuration, and evaluation protocol.

Not established: first-of-its-kind, state-of-the-art detection, superior to Jbeil/ComGA, production readiness, guaranteed attack detection, or scientific novelty from changing the community algorithm alone.

Before a thesis or paper submission, extend this review with a systematic literature search and a specific novelty assessment. Before a portfolio release, ensure that every capability and benchmark claim links to evidence from this implementation.

## References

- **R1 — Jbeil.** Khoury et al., *Jbeil: Temporal Graph-Based Inductive Learning to Infer Lateral Movement in Evolving Enterprise Networks*, IEEE Symposium on Security and Privacy, 2024. [Accessible repository][R1]; [research text](https://par.nsf.gov/servlets/purl/10540681). Verify upstream provenance before reuse; the accessible README contains inconsistent year metadata in its suggested citation.
- **R2 — LANL Auth Redteam.** [Repository README][R2]. Project description; no independent reproduction performed.
- **R3 — Lateral Movement Graph Detection.** [Repository][R3]. Synthetic demo, graph construction, frequency baseline, and path scoring.
- **R4 — ComGA.** Luo et al., *ComGA: Community-Aware Attributed Graph Anomaly Detection*, WSDM, 2022. [Repository and method description][R4].
- **R5 — Security Anomaly Detection.** [Repository][R5]. Flow-based replay and ML pipeline example; reported performance is not adopted as a benchmark here.
- **R6 — Seerflow.** [Algorithms & Detection][R6]. Documentation-level precedent for Louvain community-crossing alerts; implementation and benchmark behavior not independently verified.
- **R7 — Louvain.** [NetworkX API and original-paper reference][R7].
- **R8 — Leiden.** Traag, Waltman, and van Eck, *From Louvain to Leiden: guaranteeing well-connected communities*, Scientific Reports, 2019. [Paper][R8]; [implementation reference](https://leidenalg.readthedocs.io/en/stable/reference.html).
- **R9 — LANL Cyber1.** Kent, *Comprehensive, Multi-Source Cyber-Security Events*, 2015. [Dataset, schema, terms, and citation][R9]; DOI: 10.17021/1179829.
- **R10 — GitHub Docs.** [Licensing a repository][R10].

[R1]: https://github.com/surender08/Jbeil
[R2]: https://github.com/williammumper/lanl-auth-redteam/blob/main/README.md
[R3]: https://github.com/Saideshik/lateral-movement-graph-detection
[R4]: https://github.com/XuexiongLuoMQ/ComGA
[R5]: https://github.com/saijignas/security-anomaly-detection
[R6]: https://docs.seerflow.dev/entity-graph/algorithms/
[R7]: https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.community.louvain.louvain_communities.html
[R8]: https://doi.org/10.1038/s41598-019-41695-z
[R9]: https://csr.lanl.gov/data/cyber1/
[R10]: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository
