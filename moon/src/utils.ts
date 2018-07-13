export function getCookie(name: string) {
  const r = document.cookie.match(`\\b${name}=([^;]*)\\b`);
  return r ? r[1] : undefined;
}
