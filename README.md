<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:0891b2,50:0e7490,100:1e3a8a&height=220&section=header&text=lkun&fontSize=72&fontColor=ffffff&fontAlignY=35&desc=AI%20for%20Ocean%20Science%20%7C%20Agent%20%2B%20Scientific%20ML&descSize=18&descColor=ffffff&descAlignY=55&animation=fadeIn" />

<!--   status badges -->
<p align="center">
    <a href="https://github.com/lkun45598-lgtm/lkun45598-lgtm"><img src="https://img.shields.io/badge/status-updating-0891b2.svg"></a>
    <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.10-0e7490.svg"></a>
    <a href="https://github.com/lkun45598-lgtm?tab=repositories"><img src="https://img.shields.io/github/stars/lkun45598-lgtm?affiliations=OWNER&style=flat&logo=github&label=Total%20Stars&color=0891b2"></a>
    <a href="https://github.com/lkun45598-lgtm?tab=followers"><img src="https://img.shields.io/github/followers/lkun45598-lgtm?style=flat&logo=github&color=0e7490"></a>
</p>

<!--   typing SVG -->
<p align="center">
  <a href="https://git.io/typing-svg"><img src="https://readme-typing-svg.herokuapp.com?font=JetBrains+Mono&weight=600&size=22&duration=3000&pause=800&color=0891b2&center=true&vCenter=true&width=650&lines=Hi+there+%F0%9F%91%8B%2C+I+am+lkun;AI+for+Ocean+Science+%7C+Agent+%2B+Scientific+ML;Building+scientific+research+automation+systems;Always+learning+new+things+%F0%9F%8C%8A" alt="Typing SVG" /></a>
</p>

<!--   contact icons -->
<p align="center">
  <a href="mailto:lkun45598@gmail.com"><img align="center" src="https://img.shields.io/badge/Gmail-EA4335?style=for-the-badge&logo=gmail&logoColor=white" height="28" /></a>&nbsp;
  <a href="https://github.com/lkun45598-lgtm"><img align="center" src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" height="28" /></a>&nbsp;
  <a href="https://www.scau.edu.cn"><img align="center" src="https://img.shields.io/badge/SCAU-1e3a8a?style=for-the-badge" height="28" /></a>
</p>

<!--   navigation -->
<p align="center">
  <a href="#about"><img src="https://img.shields.io/badge/About-0891b2?style=for-the-badge" /></a>
  <a href="#tech-stack"><img src="https://img.shields.io/badge/Tech_Stack-0e7490?style=for-the-badge" /></a>
  <a href="#projects"><img src="https://img.shields.io/badge/Projects-155e75?style=for-the-badge" /></a>
  <a href="#github-stats"><img src="https://img.shields.io/badge/Stats-164e63?style=for-the-badge" /></a>
  <a href="#contact"><img src="https://img.shields.io/badge/Contact-1e3a8a?style=for-the-badge" /></a>
</p>

---

## About

- **AI undergraduate** at South China Agricultural University, focused on **Agent + scientific research automation** for ocean science
- Building end-to-end agent services that orchestrate scientific workflows — from satellite data ingestion to model training
- Current work: SST / Chl-a imputation from sparse satellite observations, ocean field super-resolution, automated loss transfer from papers to training pipelines

---

## Currently Working On

- **NZ Wavefield Super-Resolution** ([Wave_movie](https://github.com/lkun45598-lgtm/Wave_movie)) — 4× spatial super-resolution of New Zealand seismic wavefields (`50×37×3` → `200×148×3`); proposed **Wavelet-ResShift** model benchmarked against EDM / FNO / U-Net — PSNR **35.40 dB**, correlation **0.90** on 500 decoded test fields
- **Hourly SST Imputation** ([SST_Data_Imputation](https://github.com/lkun45598-lgtm/SST_Data_Imputation)) — FNO-CBAM reconstruction of cloud-occluded JAXA SST over the northern South China Sea (`451×351`); 24 per-hour models (h00–h23), OSTIA→JAXA two-stage transfer, observation-faithful output composition — *manuscript in progress*
- **Ocean Agent Platform** — FastAPI + LangGraph autoresearch service: three-layer graph orchestration (main → research → repo / migration executors) with staged gating, Human-in-the-Loop, and a self-learning experience system

---

## Tech Stack

| Property                                  | Data                                                                                                                                                                                                                                                     |
|-------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Language / Framework**                  | ![Python](https://img.shields.io/badge/-Python-3776AB?style=flat&logo=Python&logoColor=white) ![PyTorch](https://img.shields.io/badge/-PyTorch-EE4C2C?style=flat&logo=PyTorch&logoColor=white) ![TypeScript](https://img.shields.io/badge/-TypeScript-3178C6?style=flat&logo=TypeScript&logoColor=white) ![Node.js](https://img.shields.io/badge/-Node.js-339933?style=flat&logo=nodedotjs&logoColor=white) ![Express](https://img.shields.io/badge/-Express-000000?style=flat&logo=Express&logoColor=white) ![Bash](https://img.shields.io/badge/-Bash-4EAA25?style=flat&logo=GnuBash&logoColor=white) |
| **Scientific ML**                         | ![FNO](https://img.shields.io/badge/-FNO-0891b2?style=flat&logoColor=white) ![Transformer](https://img.shields.io/badge/-Transformer-0891b2?style=flat&logoColor=white) ![Diffusion](https://img.shields.io/badge/-Diffusion_Models-0891b2?style=flat&logoColor=white) ![CBAM](https://img.shields.io/badge/-CBAM-0891b2?style=flat&logoColor=white) ![SIREN](https://img.shields.io/badge/-SIREN-0891b2?style=flat&logoColor=white) ![SwinIR](https://img.shields.io/badge/-SwinIR-0891b2?style=flat&logoColor=white) |
| **Agent / Infra**                         | ![KODE SDK](https://img.shields.io/badge/-KODE_SDK-0891b2?style=flat&logoColor=white) ![SSE](https://img.shields.io/badge/-SSE-0891b2?style=flat&logoColor=white) ![Claude API](https://img.shields.io/badge/-Claude_API-191919?style=flat&logo=Anthropic&logoColor=white) ![OpenAI](https://img.shields.io/badge/-OpenAI_compat-412991?style=flat&logo=OpenAI&logoColor=white) ![DDP](https://img.shields.io/badge/-8GPU_DDP-0891b2?style=flat&logoColor=white) |
| **Ocean Data**                            | ![NetCDF](https://img.shields.io/badge/-NetCDF-0891b2?style=flat&logoColor=white) ![HDF5](https://img.shields.io/badge/-HDF5-0891b2?style=flat&logoColor=white) ![xarray](https://img.shields.io/badge/-xarray-0891b2?style=flat&logoColor=white) ![NumPy](https://img.shields.io/badge/-NumPy-013243?style=flat&logo=NumPy&logoColor=white) ![JAXA L3](https://img.shields.io/badge/-JAXA_L3-0891b2?style=flat&logoColor=white) ![ERA5](https://img.shields.io/badge/-ERA5-0891b2?style=flat&logoColor=white) ![OSTIA](https://img.shields.io/badge/-OSTIA-0891b2?style=flat&logoColor=white) |
| **Tools / CI**                            | ![Git](https://img.shields.io/badge/-Git-F05032?style=flat&logo=git&logoColor=white) ![GitHub](https://img.shields.io/badge/-GitHub-181717?style=flat&logo=github&logoColor=white) ![GitHub Actions](https://img.shields.io/badge/-GitHub_Actions-2088FF?style=flat&logo=GitHubActions&logoColor=white) ![Docker](https://img.shields.io/badge/-Docker-2496ED?style=flat&logo=docker&logoColor=white) ![VS Code](https://img.shields.io/badge/-VS_Code-007ACC?style=flat&logo=visual-studio-code&logoColor=white) ![Jupyter](https://img.shields.io/badge/-Jupyter-F37626?style=flat&logo=jupyter&logoColor=white) |

<!--   research architecture -->

<div align="center">
<h3>🌊 AI for Ocean Science</h3>
</div>

<table>
<tr>
<th align="center" width="33%">🤖 Agent Infra</th>
<th align="center" width="33%">🧠 Scientific ML</th>
<th align="center" width="33%">📡 Data Pipeline</th>
</tr>
<tr>
<td align="center" valign="top">

<img src="https://img.shields.io/badge/KODE_SDK-164e63?style=flat-square" />
<img src="https://img.shields.io/badge/Loss_Transfer-164e63?style=flat-square" /><br>
<img src="https://img.shields.io/badge/SSE_Service-164e63?style=flat-square" />
<img src="https://img.shields.io/badge/8GPU_DDP-164e63?style=flat-square" />

<br>

```
Paper → Loss Formula
→ Code Injection
→ 4-Stage Validation
→ Training Run
```

</td>
<td align="center" valign="top">

<a href="https://github.com/lkun45598-lgtm/SST_FTM"><img src="https://img.shields.io/badge/FNO--CBAM-164e63?style=flat-square" /></a>
<img src="https://img.shields.io/badge/FTM_Prior-164e63?style=flat-square" /><br>
<a href="https://github.com/lkun45598-lgtm/Ifactformer-Earthquake-Prediction"><img src="https://img.shields.io/badge/IFactFormer-164e63?style=flat-square" /></a>
<img src="https://img.shields.io/badge/Diffusion_SR-164e63?style=flat-square" />

<br>

```
Sparse Obs
→ Physical Prior + Neural Op
→ Reconstruction
→ Forecasting
```

</td>
<td align="center" valign="top">

<img src="https://img.shields.io/badge/JAXA_L3-164e63?style=flat-square" />
<img src="https://img.shields.io/badge/OSTIA-164e63?style=flat-square" /><br>
<img src="https://img.shields.io/badge/ERA5-164e63?style=flat-square" />
<img src="https://img.shields.io/badge/ECCO_LLC4320-164e63?style=flat-square" />

<br>

```
Satellite / Reanalysis
→ NetCDF → NPY
→ Validation
→ Training Pipeline
```

</td>
</tr>
</table>

---

## Projects

<div align="center">

[![Wave_movie](https://img.shields.io/badge/Wave__movie-0891b2?style=flat-square&logo=github&logoColor=white)](https://github.com/lkun45598-lgtm/Wave_movie)
[![SST_Data_Imputation](https://img.shields.io/badge/SST__Data__Imputation-0e7490?style=flat-square&logo=github&logoColor=white)](https://github.com/lkun45598-lgtm/SST_Data_Imputation)
[![SST_FTM](https://img.shields.io/badge/SST__FTM-155e75?style=flat-square&logo=github&logoColor=white)](https://github.com/lkun45598-lgtm/SST_FTM)
[![Ifactformer](https://img.shields.io/badge/Ifactformer--Earthquake-164e63?style=flat-square&logo=github&logoColor=white)](https://github.com/lkun45598-lgtm/Ifactformer-Earthquake-Prediction)
[![Ocean Agent Platform](https://img.shields.io/badge/Ocean_Agent_Platform-164e63?style=flat-square&logo=lock&logoColor=white)](https://github.com/lkun45598-lgtm)

</div>

<br>

<details>
<summary><b>Wave_movie — Wavelet-ResShift for Seismic Wavefield Super-Resolution</b></summary>
<br>

![Status](https://img.shields.io/badge/status-active-0891b2?style=flat-square)
![Stars](https://img.shields.io/github/stars/lkun45598-lgtm/Wave_movie?style=flat-square&color=0891b2)

Fourfold spatial super-resolution of New Zealand seismic wavefields. Proposes **Wavelet-ResShift**, a Swin-UNet residual-shift diffusion model operating in the wavelet domain, benchmarked against Bicubic, EDM, FNO, and U-Net baselines under a unified paper-style evaluation protocol.

| Component | Description |
|:---|:---|
| SR Task | Same-time spatial reconstruction (not forecasting): `50×37×3` → `200×148×3`, 4× per axis, on `Vx` / `Vy` / `Vz` velocity channels |
| Proposed Model | Wavelet-ResShift v5 (`UNetModelSwinWaveletV5`) — residual-shift diffusion in wavelet space |
| Baselines | Bicubic · EDM (diffusion) · FNO (neural operator) · U-Net — all evaluated in decoded physical space with fixed global amplitude stats |
| Best Results | PSNR **35.40 dB** · correlation **0.90** · RMSE 6.67×10⁻⁴ over 500 decoded full-field test samples; full-test table over 1,265 held-out samples |

- **Data**: New Zealand seismic wavefield · 3-channel velocity field · held-out event split
- **Stack**: Python · PyTorch · Swin-UNet · Wavelet Diffusion · FNO
- **[View Repository →](https://github.com/lkun45598-lgtm/Wave_movie)**

</details>

<details>
<summary><b>SST_Data_Imputation — Hourly SST Reconstruction with FNO-CBAM</b></summary>
<br>

![Status](https://img.shields.io/badge/status-active-0891b2?style=flat-square)
![Stars](https://img.shields.io/github/stars/lkun45598-lgtm/SST_Data_Imputation?style=flat-square&color=0891b2)

Deep learning system for reconstructing cloud-occluded hourly sea surface temperature over the **northern South China Sea**, combining a Fourier Neural Operator with CBAM attention and an observation-faithful output-composition scheme. Manuscript in progress.

| Component | Description |
|:---|:---|
| Task | Hourly JAXA SST gap-filling on a `451×351` grid; 30-day same-hour SST + mask sequence (60 channels) per sample |
| Preprocessing | 3-stage pipeline: time-weighted fill → σ=1.5 low-pass (fill pixels only) → 3D causal progressive KNN (k=20) |
| Per-hour Models | 24 independently fine-tuned models (h00–h23); OSTIA pretrain → hourly JAXA fine-tune two-stage transfer |
| Output Composition | Real observed pixels kept verbatim; model reconstructs only cloud-occluded pixels; σ=1.0 Gaussian applied to reconstructed pixels only → seamless, observation-preserving SST field |

- **Data**: JAXA hourly L3 SST (northern South China Sea) · OSTIA global SST
- **Stack**: Python · PyTorch · FNO · CBAM · 8-GPU DDP · LaTeX (manuscript)
- **[View Repository →](https://github.com/lkun45598-lgtm/SST_Data_Imputation)**

</details>

<details>
<summary><b>SST_FTM — Sea Surface Temperature Reconstruction with Physical Priors</b></summary>
<br>

![Status](https://img.shields.io/badge/status-active-0891b2?style=flat-square)
![Stars](https://img.shields.io/github/stars/lkun45598-lgtm/SST_FTM?style=flat-square&color=0891b2)

Physics-informed deep learning framework for SST reconstruction from cloud-contaminated satellite observations. Combines a Functional Tucker Model (FTM) for physical low-rank structure with an FNO-CBAM residual network for high-frequency detail.

| Component | Description |
|:---|:---|
| FTM Prior | Tucker decomposition + SIREN coordinate networks; learns low-rank ocean basis functions from complete OSTIA data |
| FNO-CBAM Residual | Fourier Neural Operator + channel/spatial attention; reconstructs high-frequency details on top of FTM prior |
| Two-stage Training | Stage 1: pretrain FTM on OSTIA (full coverage, 30 epochs) · Stage 2: fine-tune on JAXA L3 sparse observations (100 epochs) |
| Results | RMSE **~0.5 K** · MAE **~0.35 K** on JAXA L3 test set |

- **Data**: JAXA Himawari L3 (2015–2024, 9 years, 451×351) · OSTIA global SST
- **Stack**: Python · PyTorch · FNO · SIREN · 8-GPU DDP
- **[View Repository →](https://github.com/lkun45598-lgtm/SST_FTM)**

</details>

<details>
<summary><b>Ifactformer-Earthquake-Prediction — Seismic Wavefield Forecasting</b></summary>
<br>

![Status](https://img.shields.io/badge/status-active-0891b2?style=flat-square)
![Stars](https://img.shields.io/github/stars/lkun45598-lgtm/Ifactformer-Earthquake-Prediction?style=flat-square&color=0891b2)

Adaptation of the IFactFormer factorized Transformer architecture for long-horizon seismic wavefield prediction. Built a custom training pipeline, mmap-based dataset loader, and evaluation suite on top of the original architecture, applied to the WaveCastNet seismic dataset.

| Component | Description |
|:---|:---|
| Architecture | IFactFormer — factorized attention across spatial and temporal dimensions |
| Data | WaveCastNet · **149 GB** · 30 trajectories · 3-channel physical field · 376×256 spatial grid |
| Prediction | **460-step** autoregressive rollout from a single input frame |
| Training | 8-GPU DDP · mmap lazy-loading to handle 149 GB without full RAM load |

- **Stack**: Python · PyTorch · Factorized Transformer · 8-GPU DDP
- **[View Repository →](https://github.com/lkun45598-lgtm/Ifactformer-Earthquake-Prediction)**

</details>

<details>
<summary><b>Ocean Agent Platform — LangGraph Scientific Research Automation Service</b></summary>
<br>

![Status](https://img.shields.io/badge/status-private-164e63?style=flat-square)

A production Agent service for ocean science research automation, built on **FastAPI + LangGraph**. Exposes an SSE streaming API that drives the full research loop — conversational data preprocessing, model training, external-repo bring-up, paper-mechanism migration, and autonomous research orchestration — with Human-in-the-Loop control and a self-learning experience system.

| Component | Description |
|:---|:---|
| Autoresearch Core | Three-layer graph: `main_graph` → `research_graph` → executors; unified `PreparedContext` / `ExecutionDecision` / `ExecutionEvidence` contracts |
| Staged Gating | `quick_bringup` → `full_baseline` → `integration_experiment`, each gated on verified prior-stage evidence (no silent downgrade) |
| Repo Graph | External or internal repos → smoke + bounded train-probe → formal baseline with structured execution evidence |
| Migration Graph | Paper mechanism extraction → kernel mapping → candidate generation → alignment validation → single integration experiment |
| Universal Preprocessing | Auto-detection across **13 ocean data formats** (NetCDF / GRIB / HDF5 / …) → quality check → NPY conversion |
| Self-learning | Phase-3 diagnostic system: LLM code repair (≤3 tries) → 2-epoch validation → experience library learning + reuse |

- **Stack**: Python · FastAPI · LangGraph · SSE · PyTorch · MCP
- **Lineage**: KODE SDK (TS) → Claude Code Python SDK → LangGraph — three generations of the platform

</details>

<details>
<summary>Other repositories</summary>

<br>

| Repository | Description |
|:---|:---|
| [literature](https://github.com/lkun45598-lgtm/literature) | Team paper knowledge base — a structured, peer-reviewed literature evaluation system for scientific reading. |
| RL_for_Agent | *(private)* Loss-transfer pipeline: paper → `loss_formula.json` → code injection → 4-stage validation → training run; SwinIR val_ssim **0.6645** on 4× ocean SR. |
| [SST_Data_Imputation_2.0](https://github.com/lkun45598-lgtm/SST_Data_Imputation_2.0) | Earlier FNO-CBAM SST reconstruction iteration (single JAXA fine-tune, pre-hourly). |
| [The-homework-of-Numerical-Analysis](https://github.com/lkun45598-lgtm/The-homework-of-Numerical-Analysis) | Mathematical foundations: approximation, stability, discretization, physical modeling. |
| [Machine-Learning](https://github.com/lkun45598-lgtm/Machine-Learning) | Machine learning course work and from-scratch implementations. |
| [ML_Practice](https://github.com/lkun45598-lgtm/ML_Practice) | Hands-on machine learning practice and exercises. |
| [Statistical-Modeling](https://github.com/lkun45598-lgtm/Statistical-Modeling) | Statistical modeling course work and experiments. |
| [Algorithm_Programming](https://github.com/lkun45598-lgtm/Algorithm_Programming) | Algorithm and programming practice. |
| [Machine-Version](https://github.com/lkun45598-lgtm/Machine-Version) | Machine vision course practice and experiments. |
| [High-Speed-Rail-Ticket-Booking-Management-System.](https://github.com/lkun45598-lgtm/High-Speed-Rail-Ticket-Booking-Management-System.) | C systems practice with linked lists, persistence, and order management. |
| [PUBG-Weapon-Sound-Recognition-and-Inventory-System.](https://github.com/lkun45598-lgtm/PUBG-Weapon-Sound-Recognition-and-Inventory-System.) | ML project combining GUI, audio processing, and model training. |

</details>

---

## GitHub Stats

### GitHub Profile Trophy

<div align="center">

![Trophy](./stats/trophy.svg)

</div>

### GitHub Activity Graph

![lkun's github activity graph](https://raw.githubusercontent.com/lkun45598-lgtm/lkun45598-lgtm/output/github-contribution-grid-snake.svg#gh-light-mode-only)
![lkun's github activity graph](https://raw.githubusercontent.com/lkun45598-lgtm/lkun45598-lgtm/output/github-contribution-grid-snake-dark.svg#gh-dark-mode-only)

<div align="center">
<table>
  <tr>
    <td width="50%" align="center">
      <img src="./stats/github-stats.svg" width="100%" alt="GitHub Stats" />
    </td>
    <td width="50%" align="center">
      <img src="./stats/languages.svg" width="100%" alt="Languages" />
    </td>
  </tr>
</table>
</div>

<div align="center">

![GitHub Streak](https://streak-stats.demolab.com?user=lkun45598-lgtm&theme=dark&hide_border=true&background=0d1117&ring=0891b2&fire=06b6d4&currStreakLabel=0891b2&sideLabels=0891b2&currStreakNum=ffffff&sideNums=ffffff&dates=64748b)

</div>

<div align="center">

![Activity Graph](./stats/activity-graph.svg)

</div>

![3D Contribution Graph](./profile-3d-contrib/profile-green-animate.svg)

---

## Star History

<div align="center">

[![Star History Chart](./stats/star-history.svg)](https://star-history.com/#lkun45598-lgtm/SST_Data_Imputation&lkun45598-lgtm/SST_FTM&lkun45598-lgtm/SST_Data_Imputation_2.0&lkun45598-lgtm/Ifactformer-Earthquake-Prediction&Date)

</div>

---

## Contact

<p align="center">
  <a href="mailto:lkun45598@gmail.com"><img align="center" src="https://img.shields.io/badge/Gmail-EA4335?style=for-the-badge&logo=gmail&logoColor=white" height="30" /></a>&nbsp;
  <a href="https://github.com/lkun45598-lgtm"><img align="center" src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" height="30" /></a>
</p>

<p align="center">
  Open to research collaboration in AI for ocean science and scientific research automation.
</p>

---

<p align="center">
  <a href="https://info.flagcounter.com/"><img src="https://s01.flagcounter.com/count2/abc/bg_0d1117/txt_0891b2/border_164e63/columns_6/maxflags_12/viewers_0/labels_1/pageviews_1/flags_0/percent_0/" alt="Flag Counter" border="0"></a>
</p>

---

<div align="center">

### Thanks for visiting! ❤️

![](https://komarev.com/ghpvc/?username=lkun45598-lgtm&style=for-the-badge&color=0891b2)

*If you liked my profile, you can Star ⭐ the repo!*

</div>

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:0891b2,50:0e7490,100:1e3a8a&height=120&section=footer" />





