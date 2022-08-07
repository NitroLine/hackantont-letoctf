<template>
  <div>
    <h2>Меню доктора</h2>
    {{error}}
    <p>
    Задачи для пациента
    <el-select v-model="selectedPatientId" filterable placeholder="Пациент..">
            <el-option
                v-for="item in patients"

                :key="item.id"
                :label="item.name"
                :value="item.id"
            />
          </el-select>
    </p>
    <hr/>
    <CreateTaskForm :patient="selectedPatientId"/>
    <TasksList :patient="selectedPatientId"/>
  </div>
</template>

<script>
import CreateTaskForm from "@/components/CreateTaskForm";
import TasksList from "@/components/TasksList";

export default {
  name: "DoctorView",
  components:{CreateTaskForm, TasksList},
  data(){
    return {
      patients: [],
      selectedPatientId: "",
      error: null,
      doctorId: null,
    }
  },
  beforeMount(){
      this.getPatients(this.token).then((patients) => this.patients = patients).catch((err)=> this.error = String(err))
  },
  methods:{
    async getPatients(){
      let resp = await fetch('/pacient/');
      return await resp.json();
    }
  }
}
</script>

<style scoped>
.center{
  text-align: center;
}
</style>