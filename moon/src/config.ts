const dev = {
    api: 'http://0.0.0.0:8004',
};

const prod = {
    api: 'https://api.jifangcheng.com',
};

const config = process.env.NODE_ENV === 'production'
  ? prod
  : dev;

export default {
    // Add common config values here
    ...config
};
