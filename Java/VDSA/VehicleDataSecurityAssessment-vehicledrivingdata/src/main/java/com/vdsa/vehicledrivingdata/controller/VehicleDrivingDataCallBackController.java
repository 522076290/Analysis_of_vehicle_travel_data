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
@RequestMapping("/vehicledrivingdata/vehicledrivingdatacallback")
public class VehicleDrivingDataCallBackController extends BaseController
{
    @Autowired
    private IVehicleDrivingDataService vehicleDrivingDataService;

    /**
     * 车辆驾驶行为数据预处理
     */
    @Log(title = "车辆驾驶行为数据预处理", businessType = BusinessType.UPDATE)
    @PutMapping("/preprocessing-callback")
    public AjaxResult preprocessing(@RequestBody VehicleDrivingData vehicleDrivingData)
    {
        vehicleDrivingData.getPreprocessingState();
        return toAjax(vehicleDrivingDataService.updateVehicleDrivingData(vehicleDrivingData));
    }
}