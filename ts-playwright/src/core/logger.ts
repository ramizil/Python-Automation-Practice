// Layer 1 — a tiny shared logging helper.
// Real frameworks log what they do so failures are diagnosable from CI output
// alone. Set LOG_LEVEL=debug for verbose output; default is info.
type Level = 'debug' | 'info';

const enabled = (process.env.LOG_LEVEL ?? 'info').toLowerCase() === 'debug' ? 0 : 1;
const order: Record<Level, number> = { debug: 0, info: 1 };

export interface Logger {
  debug(msg: string, ...args: unknown[]): void;
  info(msg: string, ...args: unknown[]): void;
}

export function getLogger(name: string): Logger {
  const emit = (level: Level, msg: string, args: unknown[]) => {
    if (order[level] < enabled) return;
    // eslint-disable-next-line no-console
    console.log(`${level.toUpperCase().padEnd(5)} ${name} | ${msg}`, ...args);
  };
  return {
    debug: (msg, ...args) => emit('debug', msg, args),
    info: (msg, ...args) => emit('info', msg, args),
  };
}
