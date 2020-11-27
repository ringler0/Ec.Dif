<template>

  <div>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <p style="font-size:25px;color:green;">>>{{ mensaje }}</p>
    <p style="font-size:25px;color:blue;">>>{{ distancia }}</p>
-   <input type="button" value="ReturnServer" v-on:click="mostrarMensaje"> <br>
    lat1<input type="text" placeholder="lat1" id="txtvalor" value="52.52624809700062" > <br>
    long1<input type="text" placeholder="long1" id="txtvalor2" value="13.4197998046875" > <br> <br>
    lat2<input type="text" placeholder="lat2" id="txtvalor3" value="52.50535544522142" > <br>
    long2<input type="text" placeholder="long2" id="txtvalor4" value="13.366928100585938" > <br>

    <input type="button" value="CALCULAR DISTANCIA" v-on:click="calcularDistancia">
  </div>
</template>

<script>
import axios from 'axios'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

export default {
  name: 'Home',
  data () {
    return {mensaje: 'Aqui retorna un valor del servidor!', distancia: "Aqui retorna la distancia (km) entre dos coordenadas!"}
  },
  methods: {
    getMensaje (captura) {
      const path = 'http://localhost:5000/api/v1.0/mensaje'
      axios.get(path, {params: {var1: captura, var2: "nada"}}).then((respuesta) => {
        this.mensaje = respuesta.data
      }).catch((error) => {
        console.log(error)
      })
    },
    mostrarMensaje: function () {
      var var1 = document.getElementById('txtvalor').value
      this.getMensaje(var1)
    }, 
    calcularDistancia: function () {
      var lat1 = document.getElementById('txtvalor').value
      var long1 = document.getElementById('txtvalor2').value
      var lat2 = document.getElementById('txtvalor3').value
      var long2 = document.getElementById('txtvalor4').value

      const path = 'http://localhost:5000/point/distance/'
      axios.get(path, {params: {start_lat: lat1, start_lng: long1, end_lat: lat2, end_lng: long2 }}).then((respuesta) => {
        this.distancia=respuesta.data + " km"
      }).catch((error) => {
        console.log(error)
      })
    }
  }
}
</script>
