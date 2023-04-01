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
import com.vdsa.vehicledrivingdata.domain.VehicleDrivingData;
import com.vdsa.vehicledrivingdata.service.IVehicleDrivingDataService;
import com.vdsa.common.utils.poi.ExcelUtil;
import com.vdsa.common.core.page.TableDataInfo;

/**
 * 车辆驾驶行为数据Controller
 * 
 * @author lan
 * @date 2023-03-31
 */
@RestController
@RequestMapping("/vehicledrivingdata/vehicledrivingdata")
public class VehicleDrivingDataController extends BaseController
{
    @Autowired
    private IVehicleDrivingDataService vehicleDrivingDataService;

    /**
     * 查询车辆驾驶行为数据列表
     */
    @PreAuthorize("@ss.hasPermi('vehicledrivingdata:vehicledrivingdata:list')")
    @GetMapping("/list")
    public TableDataInfo list(VehicleDrivingData vehicleDrivingData)
    {
        startPage();
        List<VehicleDrivingData> list = vehicleDrivingDataService.selectVehicleDrivingDataList(vehicleDrivingData);
        return getDataTable(list);
    }

    /**
     * 导出车辆驾驶行为数据列表
     */
    @PreAuthorize("@ss.hasPermi('vehicledrivingdata:vehicledrivingdata:export')")
    @Log(title = "车辆驾驶行为数据", businessType = BusinessType.EXPORT)
    @PostMapping("/export")
    public void export(HttpServletResponse response, VehicleDrivingData vehicleDrivingData)
    {
        List<VehicleDrivingData> list = vehicleDrivingDataService.selectVehicleDrivingDataList(vehicleDrivingData);
        ExcelUtil<VehicleDrivingData> util = new ExcelUtil<VehicleDrivingData>(VehicleDrivingData.class);
        util.exportExcel(response, list, "车辆驾驶行为数据数据");
    }

    /**
     * 获取车辆驾驶行为数据详细信息
     */
    @PreAuthorize("@ss.hasPermi('vehicledrivingdata:vehicledrivingdata:query')")
    @GetMapping(value = "/{vehicleDataId}")
    public AjaxResult getInfo(@PathVariable("vehicleDataId") Long vehicleDataId)
    {
        return success(vehicleDrivingDataService.selectVehicleDrivingDataByVehicleDataId(vehicleDataId));
    }

    /**
     * 新增车辆驾驶行为数据
     */
    @PreAuthorize("@ss.hasPermi('vehicledrivingdata:vehicledrivingdata:add')")
    @Log(title = "车辆驾驶行为数据", businessType = BusinessType.INSERT)
    @PostMapping
    public AjaxResult add(@RequestBody VehicleDrivingData vehicleDrivingData)
    {
        return toAjax(vehicleDrivingDataService.insertVehicleDrivingData(vehicleDrivingData));
    }

    /**
     * 修改车辆驾驶行为数据
     */
    @PreAuthorize("@ss.hasPermi('vehicledrivingdata:vehicledrivingdata:edit')")
    @Log(title = "车辆驾驶行为数据", businessType = BusinessType.UPDATE)
    @PutMapping
    public AjaxResult edit(@RequestBody VehicleDrivingData vehicleDrivingData)
    {
        return toAjax(vehicleDrivingDataService.updateVehicleDrivingData(vehicleDrivingData));
    }

    /**
     * 车辆驾驶行为数据预处理
     */
    @PreAuthorize("@ss.hasPermi('vehicledrivingdata:vehicledrivingdata:edit')")
    @Log(title = "车辆驾驶行为数据预处理", businessType = BusinessType.UPDATE)
    @PutMapping("/preprocessing")
    public AjaxResult preprocessing(@RequestBody VehicleDrivingData vehicleDrivingData)
    {
        return toAjax(vehicleDrivingDataService.preprocessingVehicleDrivingData(vehicleDrivingData));
    }

    /**
     * 车辆驾驶危险行为统计
     */
    @PreAuthorize("@ss.hasPermi('vehicledrivingdata:vehicledrivingdata:edit')")
    @Log(title = "车辆驾驶行为数据预处理", businessType = BusinessType.UPDATE)
    @PutMapping("/statistics")
    public AjaxResult statistics(@RequestBody VehicleDrivingData vehicleDrivingData)
    {
        return toAjax(vehicleDrivingDataService.statisticsVehicleDrivingData(vehicleDrivingData));
    }


    /**
     * 删除车辆驾驶行为数据
     */
    @PreAuthorize("@ss.hasPermi('vehicledrivingdata:vehicledrivingdata:remove')")
    @Log(title = "车辆驾驶行为数据", businessType = BusinessType.DELETE)
	@DeleteMapping("/{vehicleDataIds}")
    public AjaxResult remove(@PathVariable Long[] vehicleDataIds)
    {
        return toAjax(vehicleDrivingDataService.deleteVehicleDrivingDataByVehicleDataIds(vehicleDataIds));
    }
}
