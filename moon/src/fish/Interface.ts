export interface Article {
  content: Array<string>;
  create_time: string;
  image_num: number;
  record_id: number;
  source: string;
  title: string;
  update_time: string;
  views: number;
}

export interface Data {
  articles: Array<Article>;
  next_page: number;
}

export interface State {
  data: Data;
}
