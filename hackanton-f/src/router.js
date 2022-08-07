import {createRouter, createWebHashHistory} from 'vue-router'
import PatientView from "@/PatientView";
import DoctorView from "@/DoctorView";

export default createRouter({
    history: createWebHashHistory(),
    routes: [
        {
            path:'/doctor',
            name: 'Doctor',
            component: DoctorView,
        },
        {
            path: '/patient',
            name: 'Patient',
            component: PatientView,
        },
    ]
})