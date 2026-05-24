---
title: "Technical Lessons"
document_type: "document"
status: "active"
version: "0.1"
created: "2026-05-23"
updated: "2026-05-23"
source_type: "internal"
provenance: "wolfpack-institutional-memory"
tags:
  - "wolfpack"
related_ids: []
append_only: false
---
# Technical Lessons

- Twilio Media Streams require JSON media events, not raw websocket audio bytes
- OpenAI Realtime emits transport-ready audio payloads
- Bidirectional realtime audio relay is required for natural conversation
- Whole-function replacement is safer than micro line edits in async websocket systems
- Render + Twilio + OpenAI Realtime architecture is operationally viable
- GitHub connector/indexing delays create execution friction
- Render free tier websocket behavior is a production risk
- Operational debugging should prioritize logs before assumptions

# Human API Doctrine

- Human API should transport artifacts, not manually engineer code
- Minimize human precision editing whenever possible
- Reduce human actions to copy/paste and deployment operations
- AI reasoning layer should generate full replacements whenever feasible
- Lowering human editing reduces deployment failure probability

# Workflow Lessons

- Persistent operational memory compounds execution speed
- Documentation must occur immediately after successful breakthroughs
- Conversational quality is more important than feature count
- Stabilize infrastructure before adding complexity
# Incident — Inline Realtime Transcription Rollback

Date: 2026-05-21

Summary:
Attempting to add OpenAI Realtime inline input_audio_transcription caused production instability. The deployed runtime rejected session.input_audio_transcription as an unknown parameter, and manual recovery attempts corrupted voice_receptionist.py through chat/GitHub paste workflows. Production was restored by replacing the file with a clean stable version and removing inline transcription.

Lessons:
- Do not use input_audio_transcription in the current OpenAI Realtime/Twilio configuration.
- Clean audio is more important than transcript capture.
- Full-file chat paste is high-risk for large Python files.
- Known-good file artifacts are safer than manual line editing.
- Use syntax checks before any deployment.
- For transcripts, prefer post-call recording/transcription instead of inline realtime transcription.

Decision:
Inline realtime transcription is rejected for v0.1. Transcript capture must move to a post-call path.
