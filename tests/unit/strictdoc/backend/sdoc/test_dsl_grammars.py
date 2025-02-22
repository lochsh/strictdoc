from typing import List

import pytest

from strictdoc.backend.sdoc.error_handling import StrictDocSemanticError
from strictdoc.backend.sdoc.models.requirement import Requirement
from strictdoc.backend.sdoc.reader import SDReader
from strictdoc.backend.source_file_syntax.reader import (
    SourceFileTraceabilityReader,
    RangePragma,
)


def test_001_additional_field_in_grammar():
    input_sdoc = """
[DOCUMENT]
TITLE: Test Document

[GRAMMAR]
ELEMENTS:
- TAG: REQUIREMENT
  FIELDS:
  - TITLE: UID
    TYPE: String
    REQUIRED: False
  - TITLE: LEVEL
    TYPE: String
    REQUIRED: False
  - TITLE: STATUS
    TYPE: String
    REQUIRED: False
  - TITLE: TAGS
    TYPE: String
    REQUIRED: False
  - TITLE: REFS
    TYPE: String
    REQUIRED: False
  - TITLE: TITLE
    TYPE: String
    REQUIRED: False
  - TITLE: STATEMENT
    TYPE: String
    REQUIRED: False
  - TITLE: RATIONALE
    TYPE: String
    REQUIRED: False
  - TITLE: COMMENT
    TYPE: String
    REQUIRED: False
  - TITLE: META_TEST
    TYPE: String
    REQUIRED: False

[REQUIREMENT]
UID: A-1
STATEMENT: >>>
the foo must bar
<<<
COMMENT: >>>
Comment
<<<
META_TEST: >>>
Yes
<<<

    """.lstrip()

    reader = SDReader()

    document = reader.read(input_sdoc)

    requirement = document.section_contents[0]
    assert isinstance(requirement, Requirement)
    for name, value in requirement.enumerate_meta_fields():
        assert value is not None
