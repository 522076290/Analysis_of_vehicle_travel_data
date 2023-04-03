package com.vdsa.vehicledrivingdata.controller;

import java.util.List;
import javax.servlet.http.HttpServletResponse;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import com.vdsa.common.annotation.Log;
import com.vdsa.common.core.controller.BaseController;
import com.vdsa.common.core.domain.AjaxResult;
import com.vdsa.common.enums.BusinessType;
import com.vdsa.vehicledrivingdata.domain.VehicleTravelMap;
import com.vdsa.vehicledrivingdata.service.IVehicleTravelMapService;
import com.vdsa.common.utils.poi.ExcelUtil;
import com.vdsa.common.core.page.TableDataInfo;

/**
 * 车辆数据地图Controller
 * 
 * @author ruoyi
 * @date 2023-04-02
 */
@RestController
@RequestMapping("/vehicledrivingmap/map")
public class VehicleTravelMapController extends BaseController
{
    @Autowired
    private IVehicleTravelMapService vehicleTravelMapService;

    /**
     * 查询车辆数据地图列表
     */
    @PreAuthorize("@ss.hasPermi('vehicledrivingmap:map:list')")
    @GetMapping("/list")
    public TableDataInfo list(VehicleTravelMap vehicleTravelMap)
    {
        startPage();
        List<VehicleTravelMap> list = vehicleTravelMapService.selectVehicleTravelMapList(vehicleTravelMap);
        return getDataTable(list);
    }

    /**
     * 导出车辆数据地图列表
     */
    @PreAuthorize("@ss.hasPermi('vehicledrivingmap:map:export')")
    @Log(title = "车辆数据地图", businessType = BusinessType.EXPORT)
    @PostMapping("/export")
    public void export(HttpServletResponse response, VehicleTravelMap vehicleTravelMap)
    {
        List<VehicleTravelMap> list = vehicleTravelMapService.selectVehicleTravelMapList(vehicleTravelMap);
        ExcelUtil<VehicleTravelMap> util = new ExcelUtil<VehicleTravelMap>(VehicleTravelMap.class);
        util.exportExcel(response, list, "车辆数据地图数据");
    }

    /**
     * 获取车辆数据地图详细信息
     */
    @PreAuthorize("@ss.hasPermi('vehicledrivingmap:map:query')")
    @GetMapping(value = "/{id}")
    public AjaxResult getInfo(@PathVariable("id") Long id)
    {
        return success(vehicleTravelMapService.selectVehicleTravelMapById(id));
    }

    /**
     * 新增车辆数据地图
     */
    @PreAuthorize("@ss.hasPermi('vehicledrivingmap:map:add')")
    @Log(title = "车辆数据地图", businessType = BusinessType.INSERT)
    @PostMapping
    public AjaxResult add(@RequestBody VehicleTravelMap vehicleTravelMap)
    {
        return toAjax(vehicleTravelMapService.insertVehicleTravelMap(vehicleTravelMap));
    }

    /**
     * 修改车辆数据地图
     */
    @PreAuthorize("@ss.hasPermi('vehicledrivingmap:map:edit')")
    @Log(title = "车辆数据地图", businessType = BusinessType.UPDATE)
    @PutMapping
    public AjaxResult edit(@RequestBody VehicleTravelMap vehicleTravelMap)
    {
        return toAjax(vehicleTravelMapService.updateVehicleTravelMap(vehicleTravelMap));
    }

    /**
     * 删除车辆数据地图
     */
    @PreAuthorize("@ss.hasPermi('vehicledrivingmap:map:remove')")
    @Log(title = "车辆数据地图", businessType = BusinessType.DELETE)
	@DeleteMapping("/{ids}")
    public AjaxResult remove(@PathVariable Long[] ids)
    {
        return toAjax(vehicleTravelMapService.deleteVehicleTravelMapByIds(ids));
    }
}
