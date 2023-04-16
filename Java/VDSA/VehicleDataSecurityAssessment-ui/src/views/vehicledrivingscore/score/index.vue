<template>
  <div class="app-container">
    <el-form :model="queryParams" ref="queryForm" size="small" :inline="true" v-show="showSearch" label-width="68px">
      <!-- <el-form-item label="对应驾驶数据id" prop="vehicleDataId">
        <el-input
          v-model="queryParams.vehicleDataId"
          placeholder="请输入对应驾驶数据id"
          clearable
          @keyup.enter.native="handleQuery"
        />
      </el-form-item> -->
      <el-form-item label="评价生成状态" prop="scoringStatus">
        <el-select v-model="queryParams.scoringStatus" placeholder="请选择评价生成状态" clearable>
          <el-option
            v-for="dict in dict.type.data_process_state"
            :key="dict.value"
            :label="dict.label"
            :value="dict.value"
          />
        </el-select>
      </el-form-item>
      <!-- <el-form-item label="安全模型得分" prop="securityModelScore">
        <el-input
          v-model="queryParams.securityModelScore"
          placeholder="请输入安全模型得分"
          clearable
          @keyup.enter.native="handleQuery"
        />
      </el-form-item>
      <el-form-item label="节能模型得分" prop="energySavingModelScore">
        <el-input
          v-model="queryParams.energySavingModelScore"
          placeholder="请输入节能模型得分"
          clearable
          @keyup.enter.native="handleQuery"
        />
      </el-form-item>
      <el-form-item label="综合模型评分" prop="compositeModelScore">
        <el-input
          v-model="queryParams.compositeModelScore"
          placeholder="请输入综合模型评分"
          clearable
          @keyup.enter.native="handleQuery"
        />
      </el-form-item> -->
      <el-form-item label="综合评价" prop="comprehensiveAssessment">
        <el-select v-model="queryParams.comprehensiveAssessment" placeholder="请选择综合评价" clearable>
          <el-option
            v-for="dict in dict.type.classify_vehicle_behavior"
            :key="dict.value"
            :label="dict.label"
            :value="dict.value"
          />
        </el-select>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" icon="el-icon-search" size="mini" @click="handleQuery">搜索</el-button>
        <el-button icon="el-icon-refresh" size="mini" @click="resetQuery">重置</el-button>
      </el-form-item>
    </el-form>

    <el-row :gutter="10" class="mb8">
      <el-col :span="1.5">
        <el-button
          type="primary"
          plain
          icon="el-icon-plus"
          size="mini"
          @click="handleAdd"
          v-hasPermi="['vehicledrivingscore:score:add']"
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
          v-hasPermi="['vehicledrivingscore:score:edit']"
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
          v-hasPermi="['vehicledrivingscore:score:remove']"
        >删除</el-button>
      </el-col>
      <el-col :span="1.5">
        <el-button
          type="warning"
          plain
          icon="el-icon-download"
          size="mini"
          @click="handleExport"
          v-hasPermi="['vehicledrivingscore:score:export']"
        >导出</el-button>
      </el-col>
      <right-toolbar :showSearch.sync="showSearch" @queryTable="getList"></right-toolbar>
    </el-row>

    <el-table v-loading="loading" :data="scoreList" @selection-change="handleSelectionChange">
      <el-table-column type="selection" width="55" align="center" />
      <!-- <el-table-column label="主键" align="center" prop="id" /> -->
      <el-table-column label="对应驾驶数据id" align="center" prop="vehicleDataId" />
      <el-table-column label="评价生成状态" align="center" prop="scoringStatus">
        <template slot-scope="scope">
          <dict-tag :options="dict.type.data_process_state" :value="scope.row.scoringStatus"/>
        </template>
      </el-table-column>
      <el-table-column label="安全模型得分" align="center" prop="securityModelScore" />
      <el-table-column label="节能模型得分" align="center" prop="energySavingModelScore" />
      <el-table-column label="综合模型评分" align="center" prop="compositeModelScore" />
      <el-table-column label="综合评价" align="center" prop="comprehensiveAssessment">
        <template slot-scope="scope">
          <dict-tag :options="dict.type.classify_vehicle_behavior" :value="scope.row.comprehensiveAssessment"/>
        </template>
      </el-table-column>
      <el-table-column label="备注" align="center" prop="remark" />
      <el-table-column label="操作" align="center" class-name="small-padding fixed-width">
        <template slot-scope="scope">
          <!-- <el-button
            size="mini"
            type="text"
            icon="el-icon-edit"
            @click="handleUpdate(scope.row)"
            v-hasPermi="['vehicledrivingscore:score:edit']"
          >修改</el-button> -->
          <el-button
            size="mini"
            type="text"
            icon="el-icon-edit"
            @click="handleClassify(scope.row)"
            v-hasPermi="['vehicledrivingscore:score:edit']"
          >分类</el-button>
          <el-button
            size="mini"
            type="text"
            icon="el-icon-delete"
            @click="handleDelete(scope.row)"
            v-hasPermi="['vehicledrivingscore:score:remove']"
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

    <!-- 添加或修改车辆驾驶行为得分对话框 -->
    <el-dialog :title="title" :visible.sync="open" width="500px" append-to-body>
      <el-form ref="form" :model="form" :rules="rules" label-width="80px">
        <el-form-item label="对应驾驶数据id" prop="vehicleDataId">
          <el-input v-model="form.vehicleDataId" placeholder="请输入对应驾驶数据id" />
        </el-form-item>
        <el-form-item label="评价生成状态" prop="scoringStatus">
          <el-select v-model="form.scoringStatus" placeholder="请选择评价生成状态">
            <el-option
              v-for="dict in dict.type.data_process_state"
              :key="dict.value"
              :label="dict.label"
              :value="parseInt(dict.value)"
            ></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="安全模型得分" prop="securityModelScore">
          <el-input v-model="form.securityModelScore" placeholder="请输入安全模型得分" />
        </el-form-item>
        <el-form-item label="节能模型得分" prop="energySavingModelScore">
          <el-input v-model="form.energySavingModelScore" placeholder="请输入节能模型得分" />
        </el-form-item>
        <el-form-item label="综合模型评分" prop="compositeModelScore">
          <el-input v-model="form.compositeModelScore" placeholder="请输入综合模型评分" />
        </el-form-item>
        <el-form-item label="综合评价" prop="comprehensiveAssessment">
          <el-input v-model="form.comprehensiveAssessment" placeholder="请输入综合评价" />
        </el-form-item>
        <el-form-item label="备注" prop="remark">
          <el-input v-model="form.remark" placeholder="请输入备注" />
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button type="primary" @click="submitForm">确 定</el-button>
        <el-button @click="cancel">取 消</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
import { listScore, getScore, delScore, addScore, updateScore ,classifyScore} from "@/api/vehicledrivingscore/score";

export default {
  name: "Score",
  dicts: ['classify_vehicle_behavior', 'data_process_state'],
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
      // 车辆驾驶行为得分表格数据
      scoreList: [],
      // 弹出层标题
      title: "",
      // 是否显示弹出层
      open: false,
      // 查询参数
      queryParams: {
        pageNum: 1,
        pageSize: 10,
        vehicleDataId: null,
        scoringStatus: null,
        securityModelScore: null,
        energySavingModelScore: null,
        compositeModelScore: null,
        comprehensiveAssessment: null,
      },
      // 表单参数
      form: {},
      // 表单校验
      rules: {
        vehicleDataId: [
          { required: true, message: "对应驾驶数据id不能为空", trigger: "blur" }
        ],
      }
    };
  },
  created() {
    this.getList();
  },
  methods: {
    /** 查询车辆驾驶行为得分列表 */
    getList() {
      this.loading = true;
      listScore(this.queryParams).then(response => {
        this.scoreList = response.rows;
        this.total = response.total;
        this.loading = false;
      });
    },
    // 取消按钮
    cancel() {
      this.open = false;
      this.reset();
    },
    // 表单重置
    reset() {
      this.form = {
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
      this.ids = selection.map(item => item.id)
      this.single = selection.length!==1
      this.multiple = !selection.length
    },
    /** 新增按钮操作 */
    handleAdd() {
      this.reset();
      this.open = true;
      this.title = "添加车辆驾驶行为得分";
    },
    /** 修改按钮操作 */
    handleUpdate(row) {
      this.reset();
      const id = row.id || this.ids
      getScore(id).then(response => {
        this.form = response.data;
        this.open = true;
        this.title = "修改车辆驾驶行为得分";
      });
    },
    /** 分类按钮操作 */
    handleClassify(row) {
      this.reset();
      const id = row.id || this.ids
      self = this
      this.$modal.confirm('是否确认提交的分类？这个过程可能会花费一些时间 请耐心等待').then(function() {
        classifyScore(id).then(response => {
          self.$modal.msgSuccess("修改成功");
          self.getList();
        });
      })
    },
    /** 提交按钮 */
    submitForm() {
      this.$refs["form"].validate(valid => {
        if (valid) {
          if (this.form.id != null) {
            updateScore(this.form).then(response => {
              this.$modal.msgSuccess("修改成功");
              this.open = false;
              this.getList();
            });
          } else {
            addScore(this.form).then(response => {
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
      const ids = row.id || this.ids;
      this.$modal.confirm('是否确认删除车辆驾驶行为得分编号为"' + ids + '"的数据项？').then(function() {
        return delScore(ids);
      }).then(() => {
        this.getList();
        this.$modal.msgSuccess("删除成功");
      }).catch(() => {});
    },
    /** 导出按钮操作 */
    handleExport() {
      this.download('vehicledrivingscore/score/export', {
        ...this.queryParams
      }, `score_${new Date().getTime()}.xlsx`)
    }
  }
};
</script>
