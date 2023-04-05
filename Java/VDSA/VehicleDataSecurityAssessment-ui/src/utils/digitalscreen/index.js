/**
 * @param {Function} fn 防抖函数
 * @param {Number} delay 延迟时间
 */
export function debounce(fn, delay) {
    var timer;
    return function () {
      var context = this;
      var args = arguments;
      clearTimeout(timer);
      timer = setTimeout(function () {
        fn.apply(context, args);
      }, delay);
    };
  }
  
  /**
   * @param {date} time 需要转换的时间
   * @param {String} fmt 需要转换的格式 如 yyyy-MM-dd、yyyy-MM-dd HH:mm:ss
   */
  export function formatTime(time, fmt) {
    if (!time) return '';//没传时间返回空
    else {
      const date = new Date(time);
      const o = {
        'M+': date.getMonth() + 1,//月
        'd+': date.getDate(),//日
        'H+': date.getHours(),//时
        'm+': date.getMinutes(),//分
        's+': date.getSeconds(),//秒
        'q+': Math.floor((date.getMonth() + 3) / 3),//月+3/3
        S: date.getMilliseconds(),//返回时间的毫秒
      };
      if (/(y+)/.test(fmt))//匹配1个到多个y
      //这一步把年转换完毕
      fmt = fmt.replace(
        RegExp.$1,//拿到y+匹配到的第一个分组
        (date.getFullYear() + '').substr(4 - RegExp.$1.length)
        );
        //这一步把生下的格式继续匹配转换
      for (const k in o) {
        if (new RegExp('(' + k + ')').test(fmt)) {
          fmt = fmt.replace(
            RegExp.$1,
            RegExp.$1.length === 1
              ? o[k]
              : ('00' + o[k]).substr(('' + o[k]).length)
          );
        }
      }
      return fmt;
    }
  }
  
  