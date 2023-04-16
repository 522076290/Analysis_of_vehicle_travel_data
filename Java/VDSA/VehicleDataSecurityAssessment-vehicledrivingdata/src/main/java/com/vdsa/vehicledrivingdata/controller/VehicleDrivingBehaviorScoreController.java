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
import com.vdsa.vehicledrivingdata.domain.VehicleDrivingBehaviorScore;
import com.vdsa.vehicledrivingdata.service.IVehicleDrivingBehaviorScoreService;
import com.vdsa.common.utils.poi.ExcelUtil;
import com.vdsa.common.core.page.TableDataInfo;

/**
 * 车辆驾驶行为得分Controller
 * 
 * @author ruoyi
 * @date 2023-04-03
 */
@RestController
@RequestMapping("/vehicledrivingscore/score")
public class VehicleDrivingBehaviorScoreController extends BaseController
{
    @Autowired
    private IVehicleDrivingBehaviorScoreService vehicleDrivingBehaviorScoreService;

    /**
     * 查询车辆驾驶行为得分列表
     */
    @PreAuthorize("@ss.hasPermi('vehicledrivingscore:score:list')")
    @GetMapping("/list")
    public TableDataInfo list(VehicleDrivingBehaviorScore vehicleDrivingBehaviorScore)
    {
        startPage();
        List<VehicleDrivingBehaviorScore> list = vehicleDrivingBehaviorScoreService.selectVehicleDrivingBehaviorScoreList(vehicleDrivingBehaviorScore);
        return getDataTable(list);
    }

    /**
     * 导出车辆驾驶行为得分列表
     */
    @PreAuthorize("@ss.hasPermi('vehicledrivingscore:score:export')")
    @Log(title = "车辆驾驶行为得分", businessType = BusinessType.EXPORT)
    @PostMapping("/export")
    public void export(HttpServletResponse response, VehicleDrivingBehaviorScore vehicleDrivingBehaviorScore)
    {
        List<VehicleDrivingBehaviorScore> list = vehicleDrivingBehaviorScoreService.selectVehicleDrivingBehaviorScoreList(vehicleDrivingBehaviorScore);
        ExcelUtil<VehicleDrivingBehaviorScore> util = new ExcelUtil<VehicleDrivingBehaviorScore>(VehicleDrivingBehaviorScore.class);
        util.exportExcel(response, list, "车辆驾驶行为得分数据");
    }

    /**
     * 获取车辆驾驶行为得分详细信息
     */
    @PreAuthorize("@ss.hasPermi('vehicledrivingscore:score:query')")
    @GetMapping(value = "/{id}")
    public AjaxResult getInfo(@PathVariable("id") Long id)
    {
        return success(vehicleDrivingBehaviorScoreService.selectVehicleDrivingBehaviorScoreById(id));
    }

    /**
     * 新增车辆驾驶行为得分
     */
    @PreAuthorize("@ss.hasPermi('vehicledrivingscore:score:add')")
    @Log(title = "车辆驾驶行为得分", businessType = BusinessType.INSERT)
    @PostMapping
    public AjaxResult add(@RequestBody VehicleDrivingBehaviorScore vehicleDrivingBehaviorScore)
    {
        return toAjax(vehicleDrivingBehaviorScoreService.insertVehicleDrivingBehaviorScore(vehicleDrivingBehaviorScore));
    }




    /**
     * 对车辆进行分类
     */
    @PreAuthorize("@ss.hasPermi('vehicledrivingscore:score:edit')")
    @Log(title = "车辆驾驶行为得分", businessType = BusinessType.UPDATE)
    @GetMapping("/classify/{id}")
    public AjaxResult classif(@PathVariable("id") Long id)
    {
        return toAjax(vehicleDrivingBehaviorScoreService.classifVehicleDrivingBehaviorScore(id));
    }



    /**
     * 修改车辆驾驶行为得分
     */
    @PreAuthorize("@ss.hasPermi('vehicledrivingscore:score:edit')")
    @Log(title = "车辆驾驶行为得分", businessType = BusinessType.UPDATE)
    @PutMapping
    public AjaxResult edit(@RequestBody VehicleDrivingBehaviorScore vehicleDrivingBehaviorScore)
    {
        return toAjax(vehicleDrivingBehaviorScoreService.updateVehicleDrivingBehaviorScore(vehicleDrivingBehaviorScore));
    }

    /**
     * 删除车辆驾驶行为得分
     */
    @PreAuthorize("@ss.hasPermi('vehicledrivingscore:score:remove')")
    @Log(title = "车辆驾驶行为得分", businessType = BusinessType.DELETE)
	@DeleteMapping("/{ids}")
    public AjaxResult remove(@PathVariable Long[] ids)
    {
        return toAjax(vehicleDrivingBehaviorScoreService.deleteVehicleDrivingBehaviorScoreByIds(ids));
    }
}
