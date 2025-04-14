"""A class to encapsulate Comic Book Lover (CBI) tag data"""

# Copyright 2012-2014 ComicTagger Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from __future__ import annotations

import logging

from comicapi.archivers import Archiver
from comicapi.comicbookinfo import ComicBookInfo
from comicapi.genericmetadata import GenericMetadata
from comicapi.tags.tag import Tag

logger = logging.getLogger(__name__)


class ComicBookLover(Tag):
    enabled = True

    id = "cbi"

    def __init__(self, version: str) -> None:
        super().__init__(version)
        self.cbi = ComicBookInfo()
        self.supported_attributes = {
            "data_origin",
            "issue_id",
            "series_id",
            "series",
            "title",
            "issue",
            "publisher",
            "month",
            "year",
            "issue_count",
            "volume",
            "volume_count",
            "comments",
            "genre",
            "language",
            "country",
            "critical_rating",
            "credits",
            "tags",
            "characters",
            "teams",
            "locations",
            "story_arcs",
        }

    def supports_tags(self, archive: Archiver) -> bool:
        """CBI tags are stored in the archive comment."""
        return archive.supports_comment()

    def has_tags(self, archive: Archiver) -> bool:
        comment = archive.get_comment()
        if comment is None:
            return False
        return self.cbi.validate_string(comment)

    def remove_tags(self, archive: Archiver) -> bool:
        if not archive.supports_comment():
            return False
        if not archive.is_writable():
            return False
        
        return archive.set_comment("")

    def read_tags(self, archive: Archiver) -> GenericMetadata:
        if not self.has_tags(archive):
            return GenericMetadata()

        comment = archive.get_comment()
        if comment is None:
            return GenericMetadata()
        
        return self.cbi.metadata_from_string(comment)

    def read_raw_tags(self, archive: Archiver) -> str:
        comment = archive.get_comment()
        if comment is None:
            return ""
        if self.cbi.validate_string(comment):
            return comment
        return ""

    def write_tags(self, metadata: GenericMetadata, archive: Archiver) -> bool:
        if not archive.is_writable():
            return False
        if not archive.supports_comment():
            return False
        
        json_string = self.cbi.string_from_metadata(metadata)
        return archive.set_comment(json_string)

    def name(self) -> str:
        return "Comic Book Lover"
