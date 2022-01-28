package DAO;

import Entity.News;

import java.util.List;

public interface NewsMapper {
    //新建一个新闻
    int save(News news);
    //根据ID查找一个新闻
    News findByID(int id);
    //根据ID删除一个新闻
    int delete(int id);
    //查找所有新闻
    List<News> findAll();
}
