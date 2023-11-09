from typing import List

from pydantic import BaseModel


class CompletionSegment(BaseModel):
    prefix: str
    suffix: str


class CompletionReq(BaseModel):
    language: str
    segments: CompletionSegment


class CompletionChoice(BaseModel):
    index: int
    text: str


class CompletionResp(BaseModel):
    id: str
    choices: List[CompletionChoice]


class EventReq(BaseModel):
    type: str
    completion_id: str
    choice_index: int


class HealthVersion(BaseModel):
    build_date: str
    build_timestamp: str
    git_sha: str
    git_describe: str


class HealthResp(BaseModel):
    model: str
    device: str
    arch: str
    cpu_info: str
    cpu_count: int
    cuda_devices: List[str]
    version: HealthVersion
