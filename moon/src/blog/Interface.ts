export interface Tags {
  user: User;
  keys: Array<string>;
  values: [string, [Tag]][];
}

export interface User {
  username: string;
  avatar: string;
  introduction: string;
  user_id: number;
}

export interface Bg {
  name: string;
  url: string;
}

export interface Tag {
  content: string;
  create_time: string;
  number: number;
  tag_id: number;
  url: string;
}

export interface Article {
  article_id: number;
  compiled_content: string;
  create_time: string;
  introduction: string;
  markdown_content: string;
  tags: Array<Tag>;
  title: string;
  update_time: string;
  user_id: number;
  views: number;
}

export interface Data {
  articles: Array<Article>;
  user: User;
  bg: Bg;
  login: boolean;
  next_page: number;
}

export interface State {
  data: Data;
  // LoadMore state
  page: string;
  tag: string;
}
