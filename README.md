<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:0891b2,50:0e7490,100:1e3a8a&height=220&section=header&text=lkun&fontSize=72&fontColor=ffffff&fontAlignY=35&desc=AI%20for%20Ocean%20Science%20%7C%20Agent%20%2B%20Scientific%20ML&descSize=18&descColor=ffffff&descAlignY=55&animation=fadeIn" />

<p align="center">
  <a href="mailto:lkun45598@gmail.com"><img src="https://img.shields.io/badge/lkun45598@gmail.com-EA4335?style=flat-square&logo=gmail&logoColor=white" /></a>
  <a href="https://github.com/lkun45598-lgtm"><img src="https://img.shields.io/badge/GitHub-lkun45598--lgtm-333333?style=flat-square&logo=github&logoColor=white" /></a>
  <a href="https://www.scau.edu.cn"><img src="https://img.shields.io/badge/SCAU-0891b2?style=flat-square" /></a>
  <img src="https://visitor-badge.laobi.icu/badge?page_id=lkun45598-lgtm.lkun45598-lgtm" alt="visitors" />
</p>

<p align="center">
  <a href="#about"><img src="https://img.shields.io/badge/About-0891b2?style=for-the-badge" /></a>
  <a href="#tech-stack"><img src="https://img.shields.io/badge/Tech_Stack-0e7490?style=for-the-badge" /></a>
  <a href="#projects"><img src="https://img.shields.io/badge/Projects-155e75?style=for-the-badge" /></a>
  <a href="#github-stats"><img src="https://img.shields.io/badge/Stats-164e63?style=for-the-badge" /></a>
  <a href="#contact"><img src="https://img.shields.io/badge/Contact-1e40af?style=for-the-badge" /></a>
</p>

---

## About

- **AI undergraduate** at South China Agricultural University, focused on **Agent + scientific research automation** for ocean science
- Building end-to-end agent services that orchestrate scientific workflows — from satellite data ingestion to model training
- Current work: SST / Chl-a imputation from sparse satellite observations, ocean field super-resolution, automated loss transfer from papers to training pipelines

---

## Currently Working On

- **Loss Transfer System** — auto-extracting loss functions from research papers and migrating them into active training runs with 4-stage validation
- **Chl-a Multi-source Fusion** — 152-channel input (SST + Chl-a + masks + coordinate encoding + physical feature engineering) for chlorophyll-a imputation
- **Ocean Agent Service** — production SSE streaming API with 8 tool sets for end-to-end scientific ML orchestration

---

## Tech Stack

<div align="center">

<table>
<tr>
<td width="33%" valign="top">

<div align="center">

[![Scientific ML](https://img.shields.io/badge/Scientific_ML-0891b2?style=flat-square)](https://github.com/lkun45598-lgtm)

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)<br>
![FNO](https://img.shields.io/badge/FNO-0891b2?style=flat-square)
![Transformer](https://img.shields.io/badge/Transformer-0891b2?style=flat-square)<br>
![Diffusion](https://img.shields.io/badge/Diffusion_Models-0891b2?style=flat-square)
![DDP](https://img.shields.io/badge/8--GPU_DDP-0891b2?style=flat-square)

</div>

</td>
<td width="33%" valign="top">

<div align="center">

[![Agent Infrastructure](https://img.shields.io/badge/Agent_Infrastructure-0891b2?style=flat-square)](https://github.com/lkun45598-lgtm/RL_for_Agent)

![Node.js](https://img.shields.io/badge/Node.js-339933?style=flat-square&logo=nodedotjs&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)<br>
![SSE](https://img.shields.io/badge/SSE-0891b2?style=flat-square)
![Express](https://img.shields.io/badge/Express-000000?style=flat-square&logo=express&logoColor=white)<br>
![KODE SDK](https://img.shields.io/badge/KODE_SDK-0891b2?style=flat-square)

</div>

</td>
<td width="33%" valign="top">

<div align="center">

[![Ocean Data](https://img.shields.io/badge/Ocean_Data-0891b2?style=flat-square)](https://github.com/lkun45598-lgtm)

![NetCDF](https://img.shields.io/badge/NetCDF-0891b2?style=flat-square)
![HDF5](https://img.shields.io/badge/HDF5-0891b2?style=flat-square)<br>
![xarray](https://img.shields.io/badge/xarray-0891b2?style=flat-square)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white)<br>
![JAXA](https://img.shields.io/badge/JAXA_L3-0891b2?style=flat-square)
![ERA5](https://img.shields.io/badge/ERA5-0891b2?style=flat-square)

</div>

</td>
</tr>
</table>

</div>

---

## Projects

<div align="center">

[![Ocean Agent Infra](https://img.shields.io/badge/Ocean_Agent_Infra-lightgrey?style=flat-square&logo=lock&logoColor=white)](https://github.com/lkun45598-lgtm)
[![RL_for_Agent](https://img.shields.io/badge/RL__for__Agent-0891b2?style=flat-square&logo=github&logoColor=white)](https://github.com/lkun45598-lgtm/RL_for_Agent)
[![SST_FTM](https://img.shields.io/badge/SST__FTM-0891b2?style=flat-square&logo=github&logoColor=white)](https://github.com/lkun45598-lgtm/SST_FTM)
[![Ifactformer](https://img.shields.io/badge/Ifactformer--Earthquake-0891b2?style=flat-square&logo=github&logoColor=white)](https://github.com/lkun45598-lgtm/Ifactformer-Earthquake-Prediction)

</div>

<br>

<details>
<summary><b>Ocean Agent Infrastructure — Scientific Research Automation Service</b></summary>
<br>

![Status](https://img.shields.io/badge/status-private-lightgrey?style=flat-square)

A production Agent HTTP service for ocean science research automation, built on KODE SDK. Provides an SSE streaming API that orchestrates the full scientific workflow — from raw satellite data ingestion to model training and experiment iteration — as a single controllable service.

| Component | Description |
|:---|:---|
| Agent Service | SSE streaming API · multi-model support (Claude / OpenAI-compat / Gemini) · session persistence |
| 8 Tool Sets | General filesystem · ocean SR preprocessing · SR training management · SST time-series preprocessing · time-series training |
| Data Validation | 3-layer declarative validation: shape contracts · land mask invariance · manifest audit |
| Training Management | Spawns and monitors 8-GPU DDP jobs for SwinIR / EDSR / FNO2d / UNet2d |
| Loss Transfer | Auto-extracts loss functions from research papers · 4-layer validation (static → smoke → single-epoch → full) |

- **Stack**: Node.js · TypeScript · KODE SDK · SSE · Python · 8-GPU DDP

</details>

<details>
<summary><b>RL_for_Agent — Loss Transfer & Experiment Automation</b></summary>
<br>

![Status](https://img.shields.io/badge/status-active-success?style=flat-square)
![Stars](https://img.shields.io/github/stars/lkun45598-lgtm/RL_for_Agent?style=flat-square)

Public interface to the ocean research automation system. The core contribution is a **Loss Transfer pipeline** that reads a research paper, extracts the loss formulation, and automatically migrates it into the active training codebase with multi-stage validation.

| Component | Description |
|:---|:---|
| Loss Transfer | Paper → `loss_formula.json` → code injection → 4-stage validation → training run |
| Ocean SR Experiments | SwinIR / EDSR / FNO2d / UNet2d on 4× ocean field super-resolution |
| Best Result | SwinIR val\_ssim **0.6645** · multi-scale relative L2 + gradient + residual FFT loss |
| Experiment Log | 50+ tracked experiments (`sandbox/results.tsv`) |

- **Stack**: Node.js · TypeScript · KODE SDK · Python · PyTorch
- **[View Repository →](https://github.com/lkun45598-lgtm/RL_for_Agent)**

</details>

<details>
<summary><b>SST_FTM — Sea Surface Temperature Reconstruction with Physical Priors</b></summary>
<br>

![Status](https://img.shields.io/badge/status-active-success?style=flat-square)
![Stars](https://img.shields.io/github/stars/lkun45598-lgtm/SST_FTM?style=flat-square)

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

![Status](https://img.shields.io/badge/status-active-success?style=flat-square)
![Stars](https://img.shields.io/github/stars/lkun45598-lgtm/Ifactformer-Earthquake-Prediction?style=flat-square)

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
<summary>Other repositories</summary>

<br>

| Repository | Description |
|:---|:---|
| [The-homework-of-Numerical-Analysis](https://github.com/lkun45598-lgtm/The-homework-of-Numerical-Analysis) | Mathematical foundations: approximation, stability, discretization, physical modeling. |
| [SST_Data_Imputation](https://github.com/lkun45598-lgtm/SST_Data_Imputation) | Earlier SST reconstruction work. |
| [SST_Data_Imputation_2.0](https://github.com/lkun45598-lgtm/SST_Data_Imputation_2.0) | Follow-up iteration on SST reconstruction. |
| [High-Speed-Rail-Ticket-Booking-Management-System.](https://github.com/lkun45598-lgtm/High-Speed-Rail-Ticket-Booking-Management-System.) | C systems practice with linked lists, persistence, and order management. |
| [PUBG-Weapon-Sound-Recognition-and-Inventory-System.](https://github.com/lkun45598-lgtm/PUBG-Weapon-Sound-Recognition-and-Inventory-System.) | ML project combining GUI, audio processing, and model training. |

</details>

---

## GitHub Stats

<div align="center">

<p>
<img src="https://github-profile-trophy.vercel.app/?username=lkun45598-lgtm&theme=radical&no-frame=true&column=6" alt="Trophy" />
</p>

</div>

![lkun's github activity graph](https://raw.githubusercontent.com/lkun45598-lgtm/lkun45598-lgtm/output/github-contribution-grid-snake.svg#gh-light-mode-only)
![lkun's github activity graph](https://raw.githubusercontent.com/lkun45598-lgtm/lkun45598-lgtm/output/github-contribution-grid-snake-dark.svg#gh-dark-mode-only)

<div align="center">

| . | . |
|---|---|
| ![lkun's github stats](https://github-readme-stats.vercel.app/api?username=lkun45598-lgtm&show_icons=true&theme=radical&include_all_commits=true&hide_border=true) | ![Top Languages](https://github-readme-stats.vercel.app/api/top-langs/?username=lkun45598-lgtm&theme=radical&layout=compact&hide_border=true&hide=jupyter%20notebook) |

</div>

<div align="center">

![GitHub Streak](https://streak-stats.demolab.com?user=lkun45598-lgtm&theme=radical&hide_border=true)

</div>

<div align="center">

![Activity Graph](https://github-readme-activity-graph.vercel.app/graph?username=lkun45598-lgtm&theme=redical&hide_border=true)

</div>

![3D Contribution Graph](./profile-3d-contrib/profile-green-animate.svg)

---

## Contact

<div align="center">

[![Email](https://img.shields.io/badge/lkun45598@gmail.com-EA4335?style=flat-square&logo=gmail&logoColor=white)](mailto:lkun45598@gmail.com)
[![GitHub](https://img.shields.io/badge/lkun45598--lgtm-333333?style=flat-square&logo=github&logoColor=white)](https://github.com/lkun45598-lgtm)

Open to research collaboration in AI for ocean science and scientific research automation.

</div>

---

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:0891b2,50:0e7490,100:1e3a8a&height=120&section=footer" />
