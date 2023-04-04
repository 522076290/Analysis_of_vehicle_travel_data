import request from '@/utils/request'

// 查询车辆数据地图列表
export function listMap(query) {
  return request({
    url: '/vehicledrivingmap/map/list',
    method: 'get',
    params: query
  })
}

// 查询车辆数据地图详细
export function getMap(id) {
  return request({
    url: '/vehicledrivingmap/map/' + id,
    method: 'get'
  })
}

// 新增车辆数据地图
export function addMap(data) {
  return request({
    url: '/vehicledrivingmap/map',
    method: 'post',
    data: data
  })
}

// 修改车辆数据地图
export function updateMap(data) {
  return request({
    url: '/vehicledrivingmap/map',
    method: 'put',
    data: data
  })
}

// 删除车辆数据地图
export function delMap(id) {
  return request({
    url: '/vehicledrivingmap/map/' + id,
    method: 'delete'
  })
}
