import axios from 'axios';

export const request = axios.create({
  baseURL: 'http://0.0.0.0:8004',
  withCredentials: true,
});
