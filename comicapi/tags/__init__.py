from __future__ import annotations

from comicapi.tags.tag import Tag

# Delay imports to avoid circular references
def get_tag_classes():
    from comicapi.tags.comicbooklover import ComicBookLover
    from comicapi.tags.comet import CoMet
    from comicapi.tags.comicrack import ComicRack
    
    return [ComicRack, ComicBookLover, CoMet]

__all__ = ["Tag"]
