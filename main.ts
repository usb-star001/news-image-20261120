// news-image-20261120 — deterministic copy program (Node 22, standard library only).
// The finished image lives beside this file as entry.png; the program copies it to
// MAKEFUN_OUTPUT_DIR/entry.png (default /output/entry.png). No network, no randomness,
// no timestamps: the same input bytes always produce the same output bytes.

import { copyFileSync, mkdirSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const here = dirname(fileURLToPath(import.meta.url));
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
mkdirSync(outDir, { recursive: true });
copyFileSync(join(here, 'entry.png'), join(outDir, 'entry.png'));
