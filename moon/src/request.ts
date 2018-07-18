import axios from 'axios';

import config from 'src/config';

export const request = axios.create({
  baseURL: config.api,
  withCredentials: true,
});
