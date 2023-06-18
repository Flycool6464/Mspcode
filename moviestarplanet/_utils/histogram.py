from __future__ import annotations

import base64, random
from typing import Optional


def GenerateHistogram() -> Optional[str]:
        '''
            Generate a random MovieStarPlanet sessionID.
        '''
        return base64.b64encode(''.join(f'{random.randint(0, 15):x}' for _ in range(48))[:46].encode()).decode()
