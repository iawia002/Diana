const dev = {
    api: 'http://0.0.0.0:8004',
};

const prod = {
    api: 'https://api.jifangcheng.com',
};

const config = process.env.REACT_APP_STAGE === 'production'
  ? prod
  : dev;

export default {
    // Add common config values here
    ...config
};
