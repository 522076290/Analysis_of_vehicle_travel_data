import request from '@/utils/request'

// 查询车辆驾驶行为得分列表
export function listScore(query) {
  return request({
    url: '/vehicledrivingscore/score/list',
    method: 'get',
    params: query
  })
}

// 查询车辆驾驶行为得分详细
export function getScore(id) {
  return request({
    url: '/vehicledrivingscore/score/' + id,
    method: 'get'
  })
}

// 新增车辆驾驶行为得分
export function addScore(data) {
  return request({
    url: '/vehicledrivingscore/score',
    method: 'post',
    data: data
  })
}

// 修改车辆驾驶行为得分
export function updateScore(data) {
  return request({
    url: '/vehicledrivingscore/score',
    method: 'put',
    data: data
  })
}


// 车辆数据分类
export function classifyScore(id) {
  return request({
    url: '/vehicledrivingscore/score/classify/'+ id,
    method: 'get',
  })
}


// 删除车辆驾驶行为得分
export function delScore(id) {
  return request({
    url: '/vehicledrivingscore/score/' + id,
    method: 'delete'
  })
}
