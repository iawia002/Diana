'use strict';

const getCookie = (name) => {
  const r = document.cookie.match(`\\b${name}=([^;]*)\\b`);
  return r ? r[1] : undefined;
}

export default {
  getCookie,
}
