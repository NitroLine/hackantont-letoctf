<template>
  <div>
    <el-empty v-if="tasks.length === 0" description="Пусто" />
    <div :key="task.date" v-for="task in tasks">
       <el-card  shadow="hover">
         <h2>
           {{ task.name }}
         </h2>
         <p>
           {{task.description}}
         </p>

       </el-card>
    </div>
  </div>
</template>

<script>
export default {
  name: "TasksList",
  props: ["patient"],
  data(){
    return {
      tasks: []
    }
  },
  beforeMount(){
    this.getTasks().then((tasks) => this.tasks = tasks).catch((err) => this.error = String(err));
  },
  methods:{
    async getTasks(){
      let result = [
        {name: 'Выпить таблетки', date: '12:22 12 сентября', description: "3 грамма для деда", done: true},
        {name: 'Выпить таблетки', date: '13:22 12 сентября ', description: "грамма для деда"}
      ];
      return result
    },
  },
}
</script>

<style scoped>

</style>