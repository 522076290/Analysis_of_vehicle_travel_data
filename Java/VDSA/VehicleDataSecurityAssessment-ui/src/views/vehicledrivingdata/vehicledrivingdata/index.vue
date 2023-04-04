<template>
  <div class="app-container">
    <!-- <el-form :model="queryParams" ref="queryForm" size="small" :inline="true" v-show="showSearch" label-width="68px">
      <el-form-item label="急加速次数" prop="rapidAccNumbers">
        <el-input
          v-model="queryParams.rapidAccNumbers"
          placeholder="请输入急加速次数"
          clearable
          @keyup.enter.native="handleQuery"
        />
      </el-form-item>
      <el-form-item label="急加速时长" prop="rapidAccDuration">
        <el-input
          v-model="queryParams.rapidAccDuration"
          placeholder="请输入急加速时长"
          clearable
          @keyup.enter.native="handleQuery"
        />
      </el-form-item>
      <el-form-item label="急减速次数" prop="rapidDecNumbers">
        <el-input
          v-model="queryParams.rapidDecNumbers"
          placeholder="请输入急减速次数"
          clearable
          @keyup.enter.native="handleQuery"
        />
      </el-form-item>
      <el-form-item label="急减速时长" prop="rapidDecDuration">
        <el-input
          v-model="queryParams.rapidDecDuration"
          placeholder="请输入急减速时长"
          clearable
          @keyup.enter.native="handleQuery"
        />
      </el-form-item>
      <el-form-item label="熄火滑行次数" prop="slideFrameoutNumbers">
        <el-input
          v-model="queryParams.slideFrameoutNumbers"
          placeholder="请输入熄火滑行次数"
          clearable
          @keyup.enter.native="handleQuery"
        />
      </el-form-item>
      <el-form-item label="熄火滑行时长" prop="slideFrameoutDuration">
        <el-input
          v-model="queryParams.slideFrameoutDuration"
          placeholder="请输入熄火滑行时长"
          clearable
          @keyup.enter.native="handleQuery"
        />
      </el-form-item>
      <el-form-item label="超速次数" prop="overspeedNumbers">
        <el-input
          v-model="queryParams.overspeedNumbers"
          placeholder="请输入超速次数"
          clearable
          @keyup.enter.native="handleQuery"
        />
      </el-form-item>
      <el-form-item label="超速时长" prop="overspeedDuration">
        <el-input
          v-model="queryParams.overspeedDuration"
          placeholder="请输入超速时长"
          clearable
          @keyup.enter.native="handleQuery"
        />
      </el-form-item>
      <el-form-item label="疲劳驾驶次数" prop="fatiguedrivingNumbers">
        <el-input
          v-model="queryParams.fatiguedrivingNumbers"
          placeholder="请输入疲劳驾驶次数"
          clearable
          @keyup.enter.native="handleQuery"
        />
      </el-form-item>
      <el-form-item label="疲劳驾驶时长" prop="fatiguedrivingHours">
        <el-input
          v-model="queryParams.fatiguedrivingHours"
          placeholder="请输入疲劳驾驶时长"
          clearable
          @keyup.enter.native="handleQuery"
        />
      </el-form-item>
      <el-form-item label="急转弯次数" prop="suddenturnNumbers">
        <el-input
          v-model="queryParams.suddenturnNumbers"
          placeholder="请输入急转弯次数"
          clearable
          @keyup.enter.native="handleQuery"
        />
      </el-form-item>
      <el-form-item label="怠速预热次数" prop="idlePreheatingNumbers">
        <el-input
          v-model="queryParams.idlePreheatingNumbers"
          placeholder="请输入怠速预热次数"
          clearable
          @keyup.enter.native="handleQuery"
        />
      </el-form-item>
      <el-form-item label="怠速预热时长" prop="idlePreheatingMins">
        <el-input
          v-model="queryParams.idlePreheatingMins"
          placeholder="请输入怠速预热时长"
          clearable
          @keyup.enter.native="handleQuery"
        />
      </el-form-item>
      <el-form-item label="超长怠速次数" prop="overlongIdleNumbers">
        <el-input
          v-model="queryParams.overlongIdleNumbers"
          placeholder="请输入超长怠速次数"
          clearable
          @keyup.enter.native="handleQuery"
        />
      </el-form-item>
      <el-form-item label="超长怠速时长" prop="overlongIdleMins">
        <el-input
          v-model="queryParams.overlongIdleMins"
          placeholder="请输入超长怠速时长"
          clearable
          @keyup.enter.native="handleQuery"
        />
      </el-form-item>
      <el-form-item>
        <el-button type="primary" icon="el-icon-search" size="mini" @click="handleQuery">搜索</el-button>
        <el-button icon="el-icon-refresh" size="mini" @click="resetQuery">重置</el-button>
      </el-form-item>
    </el-form> -->

    <el-row :gutter="10" class="mb8">
      <el-col :span="1.5">
        <el-button
          type="primary"
          plain
          icon="el-icon-plus"
          size="mini"
          @click="handleAdd"
          v-hasPermi="['vehicledrivingdata:vehicledrivingdata:add']"
        >新增</el-button>
      </el-col>
      <el-col :span="1.5">
        <el-button
          type="success"
          plain
          icon="el-icon-edit"
          size="mini"
          :disabled="single"
          @click="handleUpdate"
          v-hasPermi="['vehicledrivingdata:vehicledrivingdata:edit']"
        >修改</el-button>
      </el-col>
      <el-col :span="1.5">
        <el-button
          type="danger"
          plain
          icon="el-icon-delete"
          size="mini"
          :disabled="multiple"
          @click="handleDelete"
          v-hasPermi="['vehicledrivingdata:vehicledrivingdata:remove']"
        >删除</el-button>
      </el-col>
      <el-col :span="1.5">
        <el-button
          type="warning"
          plain
          icon="el-icon-download"
          size="mini"
          @click="handleExport"
          v-hasPermi="['vehicledrivingdata:vehicledrivingdata:export']"
        >导出</el-button>
      </el-col>
      <right-toolbar :showSearch.sync="showSearch" @queryTable="getList"></right-toolbar>
    </el-row>

    <el-table v-loading="loading" :data="vehicledrivingdataList" @selection-change="handleSelectionChange">
      <el-table-column type="selection" width="55" align="center" />
      <el-table-column label="车辆行驶数据编号" align="center" prop="vehicleDataId" />
      <el-table-column label="车辆数据文件" align="center" prop="dataPath"  :formatter="fileNameFormat"/>
      <el-table-column label="总里程" align="center" prop="totalDistance" />
      <el-table-column label="实际驾驶时间" align="center" prop="drivingTime" />
      <el-table-column label="平均驾驶速度" align="center" prop="meanSpeed" />
      <el-table-column label="车速方差" align="center" prop="speedStd" />
      <el-table-column label="急加速次数" align="center" prop="rapidAccNumbers" />
      <!-- <el-table-column label="急加速时长" align="center" prop="rapidAccDuration" /> -->
      <el-table-column label="急减速次数" align="center" prop="rapidDecNumbers" />
      <el-table-column label="急减速时长" align="center" prop="rapidDecDuration" />
      <el-table-column label="熄火滑行次数" align="center" prop="slideFrameoutNumbers" />
      <!-- <el-table-column label="熄火滑行时长" align="center" prop="slideFrameoutDuration" /> -->
      <el-table-column label="超速次数" align="center" prop="overspeedNumbers" />
      <!-- <el-table-column label="超速时长" align="center" prop="overspeedDuration" /> -->
      <el-table-column label="疲劳驾驶次数" align="center" prop="fatiguedrivingNumbers" />
      <!-- <el-table-column label="疲劳驾驶时长" align="center" prop="fatiguedrivingHours" /> -->
      <el-table-column label="急转弯次数" align="center" prop="suddenturnNumbers" />
      <el-table-column label="怠速预热次数" align="center" prop="idlePreheatingNumbers" />
      <el-table-column label="怠速预热时长" align="center" prop="idlePreheatingMins" />
      <el-table-column label="超长怠速次数" align="center" prop="overlongIdleNumbers" />
      <!-- <el-table-column label="超长怠速时长" align="center" prop="overlongIdleMins" /> -->
      <el-table-column label="预处理状态" align="center" prop="preprocessingState">
        <template slot-scope="scope">
          <dict-tag :options="dict.type.data_process_state" :value="scope.row.preprocessingState"/>
        </template>
      </el-table-column>
      <el-table-column label="统计状态" align="center" prop="statisticalState">
        <template slot-scope="scope">
          <dict-tag :options="dict.type.data_process_state" :value="scope.row.statisticalState"/>
        </template>
      </el-table-column>
      <el-table-column label="操作" align="center" class-name="small-padding fixed-width">
        <template slot-scope="scope">
          <el-button
            size="mini"
            type="text"
            icon="el-icon-edit"
            @click="handlePreprocessing(scope.row)"
            v-show="scope.row.preprocessingState == 0"
            v-hasPermi="['vehicledrivingdata:vehicledrivingdata:edit']"
          >数据预处理</el-button>
          <el-button
            size="mini"
            type="text"
            icon="el-icon-edit"
            @click="handleUpdate(scope.row)"
            v-hasPermi="['vehicledrivingdata:vehicledrivingdata:edit']"
          >查看详情</el-button>
          <el-button
            size="mini"
            type="text"
            icon="el-icon-edit"
            @click="handleStatistics(scope.row)"
            v-hasPermi="['vehicledrivingdata:vehicledrivingdata:edit']"
          >危险行为统计</el-button>
          <el-button
            size="mini"
            type="text"
            icon="el-icon-edit"
            @click="handleDrawMap(scope.row)"
            v-hasPermi="['vehicledrivingmap:map:edit']"
          >绘制地图</el-button>
          <el-button
            size="mini"
            type="text"
            icon="el-icon-edit"
            v-show="scope.row.statisticalState == 2"
            @click="handleScore(scope.row)"
            v-hasPermi="['vehicledrivingscore:score:edit']"
          >安全得分计算</el-button>
          <el-button
            size="mini"
            type="text"
            icon="el-icon-delete"
            @click="handleDelete(scope.row)"
            v-hasPermi="['vehicledrivingdata:vehicledrivingdata:remove']"
          >删除</el-button>
        </template>
      </el-table-column>
    </el-table>
    
    <pagination
      v-show="total>0"
      :total="total"
      :page.sync="queryParams.pageNum"
      :limit.sync="queryParams.pageSize"
      @pagination="getList"
    />

    <!-- 查看车辆数据详情 -->
    <el-dialog :title="detailtitle" :visible.sync="detailopen" width="500px" append-to-body>
      <el-form ref="form" :model="form" :rules="rules" label-width="80px">
        <!-- <el-form-item label="对应用户id" prop="userId">
          <el-input v-model="form.userId" placeholder="请输入对应用户id" />
        </el-form-item>
        <el-form-item label="文件上传地址" prop="dataPath">
          <file-upload v-model="form.dataPath"/>
        </el-form-item> -->
        <el-row>
          <el-col :span="12">
            <el-form-item label="总里程" prop="totalDistance" label-width="100px" class="form-label">
              {{ form.totalDistance }} 公里
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="驾驶时间" prop="drivingTime" label-width="100px" class="form-label">
              {{ form.drivingTime }} /h
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="驾驶速度" prop="meanSpeed" label-width="100px" class="form-label">
              {{ form.meanSpeed }} 公里/h
            </el-form-item>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="12">
            <el-form-item label="急加速次数" prop="rapidAccNumbers" label-width="100px" class="form-label">
              {{ form.rapidAccNumbers }} 次
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="急加速时长" prop="rapidAccDuration" label-width="100px" class="form-label">
              {{ form.rapidAccDuration }} 秒
            </el-form-item>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="12">
            <el-form-item label="急减速次数" prop="rapidDecNumbers" label-width="100px" class="form-label">
              {{ form.rapidDecNumbers }} 次
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="急减速时长" prop="rapidDecDuration" label-width="100px" class="form-label">
              {{ form.rapidDecDuration }} 秒
            </el-form-item>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="12">
            <el-form-item label="熄火滑行次数" prop="slideFrameoutNumbers" label-width="100px" class="form-label">
              {{ form.slideFrameoutNumbers }} 次
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="熄火滑行时长" prop="slideFrameoutDuration" label-width="100px" class="form-label">
              {{ form.slideFrameoutDuration }} 秒
            </el-form-item>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="12">
            <el-form-item label="超速次数" prop="overspeedNumbers" label-width="100px" class="form-label">
              {{ form.overspeedNumbers }} 次
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="超速时长" prop="overspeedDuration" label-width="100px" class="form-label">
              {{ form.overspeedDuration }} 秒
            </el-form-item>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="12">
            <el-form-item label="疲劳驾驶次数" prop="fatiguedrivingNumbers" label-width="100px" class="form-label">
              {{ form.fatiguedrivingNumbers }} 次
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="疲劳驾驶时长" prop="fatiguedrivingHours" label-width="100px" class="form-label">
              {{ form.fatiguedrivingHours }} 秒
            </el-form-item>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="24">
            <el-form-item label="急转弯次数" prop="suddenturnNumbers" label-width="100px" class="form-label">
              {{ form.suddenturnNumbers }} 次
            </el-form-item>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="12">
            <el-form-item label="怠速预热次数" prop="idlePreheatingNumbers" label-width="100px" class="form-label">
              {{ form.idlePreheatingNumbers }} 秒
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="怠速预热时长" prop="idlePreheatingMins" label-width="100px" class="form-label">
              {{ form.idlePreheatingMins }} 秒
            </el-form-item>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="12">
            <el-form-item label="超长怠速次数" prop="overlongIdleNumbers" label-width="100px" class="form-label">
              {{ form.overlongIdleNumbers }} 秒
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="超长怠速时长" prop="overlongIdleMins" label-width="100px" class="form-label">
              {{ form.overlongIdleMins }} 秒
            </el-form-item>
          </el-col>
        </el-row>

      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button type="primary" @click="cancel">确 定</el-button>
        <el-button @click="cancel">取 消</el-button>
      </div>
    </el-dialog>


    <!-- 添加或者修改车辆数据详情 -->
    <el-dialog :title="title" :visible.sync="open" width="500px" append-to-body>
      <el-form ref="form" :model="form" :rules="rules" label-width="80px">
        <!-- <el-form-item label="对应用户id" prop="userId">
          <el-input v-model="form.userId" placeholder="请输入对应用户id" />
        </el-form-item> -->
        <el-form-item label="文件上传地址" prop="dataPath">
          <file-upload v-model="form.dataPath"/>
        </el-form-item>
        <!-- <el-form-item label="急加速次数" prop="rapidAccNumbers">
          <el-input v-model="form.rapidAccNumbers" placeholder="请输入急加速次数" />
        </el-form-item>
        <el-form-item label="急加速时长" prop="rapidAccDuration">
          <el-input v-model="form.rapidAccDuration" placeholder="请输入急加速时长" />
        </el-form-item>
        <el-form-item label="急减速次数" prop="rapidDecNumbers">
          <el-input v-model="form.rapidDecNumbers" placeholder="请输入急减速次数" />
        </el-form-item>
        <el-form-item label="急减速时长" prop="rapidDecDuration">
          <el-input v-model="form.rapidDecDuration" placeholder="请输入急减速时长" />
        </el-form-item> -->
        <!-- <el-form-item label="熄火滑行次数" prop="slideFrameoutNumbers">
          <el-input v-model="form.slideFrameoutNumbers" placeholder="请输入熄火滑行次数" />
        </el-form-item>
        <el-form-item label="熄火滑行时长" prop="slideFrameoutDuration">
          <el-input v-model="form.slideFrameoutDuration" placeholder="请输入熄火滑行时长" />
        </el-form-item> -->
        <!-- <el-form-item label="超速次数" prop="overspeedNumbers">
          <el-input v-model="form.overspeedNumbers" placeholder="请输入超速次数" />
        </el-form-item>
        <el-form-item label="超速时长" prop="overspeedDuration">
          <el-input v-model="form.overspeedDuration" placeholder="请输入超速时长" />
        </el-form-item> -->
        <!-- <el-form-item label="疲劳驾驶次数" prop="fatiguedrivingNumbers">
          <el-input v-model="form.fatiguedrivingNumbers" placeholder="请输入疲劳驾驶次数" />
        </el-form-item>
        <el-form-item label="疲劳驾驶时长" prop="fatiguedrivingHours">
          <el-input v-model="form.fatiguedrivingHours" placeholder="请输入疲劳驾驶时长" />
        </el-form-item> -->
        <!-- <el-form-item label="急转弯次数" prop="suddenturnNumbers">
          <el-input v-model="form.suddenturnNumbers" placeholder="请输入急转弯次数" />
        </el-form-item>
        <el-form-item label="怠速预热次数" prop="idlePreheatingNumbers">
          <el-input v-model="form.idlePreheatingNumbers" placeholder="请输入怠速预热次数" />
        </el-form-item>
        <el-form-item label="怠速预热时长" prop="idlePreheatingMins">
          <el-input v-model="form.idlePreheatingMins" placeholder="请输入怠速预热时长" />
        </el-form-item> -->
        <!-- <el-form-item label="超长怠速次数" prop="overlongIdleNumbers">
          <el-input v-model="form.overlongIdleNumbers" placeholder="请输入超长怠速次数" />
        </el-form-item>
        <el-form-item label="超长怠速时长" prop="overlongIdleMins">
          <el-input v-model="form.overlongIdleMins" placeholder="请输入超长怠速时长" />
        </el-form-item> -->
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button type="primary" @click="submitForm">确 定</el-button>
        <el-button @click="cancel">取 消</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
import { listVehicledrivingdata, getVehicledrivingdata, delVehicledrivingdata, addVehicledrivingdata, updateVehicledrivingdata, preprocessingVehicledrivingdata, statisticsVehicledrivingdata } from "@/api/vehicledrivingdata/vehicledrivingdata";
import {  addMap } from "@/api/vehicledrivingmap/map";
import { addScore } from "@/api/vehicledrivingscore/score";

export default {
  name: "Vehicledrivingdata",
  dicts: ['data_process_state'],
  data() {
    return {
      // 遮罩层
      loading: true,
      // 选中数组
      ids: [],
      // 非单个禁用
      single: true,
      // 非多个禁用
      multiple: true,
      // 显示搜索条件
      showSearch: true,
      // 总条数
      total: 0,
      // 车辆驾驶行为数据表格数据
      vehicledrivingdataList: [],
      // 添加弹出层标题
      title: "",
      // 详情弹出层标题
      detailtitle: "",
      // 是否显示添加弹出层
      open: false,
      // 是否显示详情弹出层
      detailopen: false,
      // 查询参数
      queryParams: {
        pageNum: 1,
        pageSize: 10,
        userId: null,
        dataPath: null,
        totalDistance: null,
        drivingTime: null,
        meanSpeed: null,
        speedStd: null,
        rapidAccNumbers: null,
        rapidAccDuration: null,
        rapidDecNumbers: null,
        rapidDecDuration: null,
        slideFrameoutNumbers: null,
        slideFrameoutDuration: null,
        overspeedNumbers: null,
        overspeedDuration: null,
        fatiguedrivingNumbers: null,
        fatiguedrivingHours: null,
        suddenturnNumbers: null,
        idlePreheatingNumbers: null,
        idlePreheatingMins: null,
        overlongIdleNumbers: null,
        overlongIdleMins: null,
        preprocessingState: null,
        statisticalState: null
      },
      // 表单参数
      form: {},
      mapform: {
        id: null,
        vehicleDataId: null,
        mapPath: null,
        buildMapStatus: null,
        createBy: null,
        createTime: null,
        updateBy: null,
        updateTime: null,
        remark: null
      },
      scorefrom: {
        id: null,
        vehicleDataId: null,
        scoringStatus: null,
        securityModelScore: null,
        energySavingModelScore: null,
        compositeModelScore: null,
        comprehensiveAssessment: null,
        createBy: null,
        createTime: null,
        updateBy: null,
        updateTime: null,
        remark: null
      },
      // 表单校验
      rules: {
        userId: [
          { required: true, message: "对应用户id不能为空", trigger: "blur" }
        ],
        dataPath: [
          { required: true, message: "文件上传地址不能为空", trigger: "blur" }
        ],
      }
    };
  },
  created() {
    this.getList();
  },
  methods: {
    /** 查询车辆驾驶行为数据列表 */
    getList() {
      this.loading = true;
      listVehicledrivingdata(this.queryParams).then(response => {
        this.vehicledrivingdataList = response.rows;
        this.total = response.total;
        this.loading = false;
      });
    },
    // 取消按钮
    cancel() {
      this.open = false;
      this.detailopen = false;
      this.reset();
    },
    // 表单重置
    reset() {
      this.form = {
        vehicleDataId: null,
        userId: null,
        dataPath: null,
        totalDistance: null,
        drivingTime: null,
        meanSpeed: null,
        speedStd: null,
        rapidAccNumbers: null,
        rapidAccDuration: null,
        rapidDecNumbers: null,
        rapidDecDuration: null,
        slideFrameoutNumbers: null,
        slideFrameoutDuration: null,
        overspeedNumbers: null,
        overspeedDuration: null,
        fatiguedrivingNumbers: null,
        fatiguedrivingHours: null,
        suddenturnNumbers: null,
        idlePreheatingNumbers: null,
        idlePreheatingMins: null,
        overlongIdleNumbers: null,
        overlongIdleMins: null,
        preprocessingState: null,
        statisticalState: null
      };
      this.resetForm("form");
    },
    /** 搜索按钮操作 */
    handleQuery() {
      this.queryParams.pageNum = 1;
      this.getList();
    },
    /** 重置按钮操作 */
    resetQuery() {
      this.resetForm("queryForm");
      this.handleQuery();
    },
    // 多选框选中数据
    handleSelectionChange(selection) {
      this.ids = selection.map(item => item.vehicleDataId)
      this.single = selection.length!==1
      this.multiple = !selection.length
    },
    /** 新增按钮操作 */
    handleAdd() {
      this.reset();
      this.open = true;
      this.title = "添加车辆驾驶行为数据";
    },
    /** 修改按钮操作 */
    handleUpdate(row) {
      this.reset();
      const vehicleDataId = row.vehicleDataId || this.ids
      getVehicledrivingdata(vehicleDataId).then(response => {
        this.form = response.data;
        this.detailopen = true;
        this.detailtitle = "查看车辆驾驶行为数据";
      });
    },
    /** 数据预处理按钮操作 */
    handlePreprocessing(row) {
      this.reset();
      const vehicleDataId = row.vehicleDataId || this.ids
      const fileName = row.fileName || this.fileNameFormat(row)
      const self = this;
      this.$modal.confirm('是否确认提交"' + fileName + '"的数据进行预处理？这个过程可能会花费一些时间 请耐心等待').then(function() {
        getVehicledrivingdata(vehicleDataId).then(response => {
          preprocessingVehicledrivingdata(response.data).then(() => {
            self.getList()
            self.$modal.msgSuccess("提交预处理成功")
          }).catch(() => {});
        });
      })
    },
    /** 危险行为统计按钮操作 */
    handleStatistics(row) {
      this.reset();
      const vehicleDataId = row.vehicleDataId || this.ids
      const fileName = row.fileName || this.fileNameFormat(row)
      const self = this;
      this.$modal.confirm('是否确认提交"' + fileName + '"的数据进行统计？这个过程可能会花费一些时间 请耐心等待').then(function() {
        getVehicledrivingdata(vehicleDataId).then(response => {
          statisticsVehicledrivingdata(response.data).then(() => {
            self.getList()
            self.$modal.msgSuccess("提交危险统计成功")
          }).catch(() => {});
        });
      })
    },
    /** 地图绘制按钮操作 */
    handleDrawMap(row) {
      this.reset();
      const vehicleDataId = row.vehicleDataId || this.ids
      const fileName = row.fileName || this.fileNameFormat(row)
      const self = this;
      this.$modal.confirm('是否确认提交"' + fileName + '"的数据进行地图绘制？ 这个过程可能会花费一些时间 请耐心等待').then(function() {
        self.mapform.vehicleDataId =vehicleDataId
        addMap(self.mapform).then(response => {
          self.getList()
          self.$modal.msgSuccess("提交地图绘制成功")
          });
      })
    },
    /** 车辆安全得分计算按钮 */
    handleScore(row) {
      this.reset();
      const vehicleDataId = row.vehicleDataId || this.ids
      const fileName = row.fileName || this.fileNameFormat(row)
      const self = this;
      this.$modal.confirm('是否确认提交"' + fileName + '"的数据进行得分计算？ 这个过程可能会花费一些时间 请耐心等待').then(function() {
        self.scorefrom.vehicleDataId =vehicleDataId
        addScore(self.scorefrom).then(response => {
          self.getList()
          self.$modal.msgSuccess("提交得分计算成功")
          });
      })
    },
    /** 提交按钮 */
    submitForm() {
      this.$refs["form"].validate(valid => {
        if (valid) {
          if (this.form.vehicleDataId != null) {
            updateVehicledrivingdata(this.form).then(response => {
              this.$modal.msgSuccess("修改成功");
              this.open = false;
              this.getList();
            });
          } else {
            addVehicledrivingdata(this.form).then(response => {
              this.$modal.msgSuccess("新增成功");
              this.open = false;
              this.getList();
            });
          }
        }
      });
    },
    /** 删除按钮操作 */
    handleDelete(row) {
      const vehicleDataIds = row.vehicleDataId || this.ids;
      this.$modal.confirm('是否确认删除车辆驾驶行为数据编号为"' + vehicleDataIds + '"的数据项？').then(function() {
        return delVehicledrivingdata(vehicleDataIds);
      }).then(() => {
        this.getList();
        this.$modal.msgSuccess("删除成功");
      }).catch(() => {});
    },
    /** 导出按钮操作 */
    handleExport() {
      this.download('vehicledrivingdata/vehicledrivingdata/export', {
        ...this.queryParams
      }, `vehicledrivingdata_${new Date().getTime()}.xlsx`)
    },
    fileNameFormat(row, column) {
      return row.dataPath.match(/[^/]+$/)[0]
    }
  }
};
</script>
<style>
.form-label label {
  font-size: 14px;
}
</style>