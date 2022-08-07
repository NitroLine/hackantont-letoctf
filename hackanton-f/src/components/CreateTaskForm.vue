<template>
  <div class="center">
  <p>
        <el-button type="primary" size="large" @click="modal = true" :icon="Plus" :disabled="!patient">Добавить задачу</el-button>
    </p>
    <el-dialog v-model="modal" title="Добавить таск">
      <el-form :model="form">
        <el-form-item label="Заголовок" :label-width="formLabelWidth">
          <el-input v-model="form.title" autocomplete="off" />
        </el-form-item>
        <el-form-item label="Описание" :label-width="formLabelWidth">
          <el-input
              v-model="form.descritption"
              :autosize="{ minRows: 2, maxRows: 4 }"
              type="textarea"
              placeholder="Описание для задачи"
          />
        </el-form-item>
        <el-form-item label="Дата" :label-width="formLabelWidth">
          <el-date-picker
              v-model="form.date"
              type="datetime"
              placeholder="Выбирите дату и время "
          />
          </el-form-item>
      </el-form>
    <template #footer>
      <span class="dialog-footer">
        <el-button @click="modal = false">Отмена</el-button>
        <el-button type="primary" @click="createTask"
          >Создать</el-button
        >
      </span>
    </template>
  </el-dialog>
  </div>
</template>
<script setup>
import { Plus } from '@element-plus/icons-vue'
</script>

<script>

export default {
  name: "CreateTaskForm",
  props:["patient"],
  data(){
    return {
      formLabelWidth: undefined,
      form: {
        title: "",
        description: "",
        date: "",
      },
      modal: false,
    }
  },
  methods: {
    createTask(){
      // req here
      const body = {
        "title": this.form.title,
        "time": this.form.time,
        "description": this.form.description,
        "doctor": this.$route.query.id,
        "pacient": this.patient,
        "status": false,
      }
      fetch('/task/', {
        body: JSON.stringify(body),
        method: "POST",
        headers: {
          Accept: "application/json",
          "Content-Type": "application/json",
        },
      });
      console.log(this.form.title, this.form.date)
      this.modal = false;
      this.form.title = ""
      this.form.description = "";
      this.form.date = "";
    }
  }
}
</script>

<style scoped>
  .center{
    text-align: center;
  }
</style>