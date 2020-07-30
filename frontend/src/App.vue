<template>
  <div id="app">
    <header>
      <img height="65" alt="Sigma logo" src="./assets/logo.png">
    </header>
    <h1 class="font-weight-bold">Prueba de desarrollo Sigma</h1>
    <div id="text" class="mx-auto">
      <p>
        Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the<br>
        industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type
        and<br> scrambled it to make a type specimen book.
      </p>
    </div>
    <div class="container" id="container">
      <div class="row">
        <div class="col-lg px-0">
          <img id="image" src="./assets/image.png" style="max-width:436px">
        </div>
        <div class="col-lg">
          <form @submit.prevent="submit" :class="{'was-validated': wasValidated}" novalidate>
            <div class="form-group">
              <label for="state" class="font-weight-bold">Departamento*</label>
              <select class="custom-select mb-0" id="state" required v-model="contact.state">
                <option value="" v-if="!contact.state">Antioquia</option>
                <option v-for="(cities, name) in states" :value="name" :key="name">
                  {{ name }}
                </option>
              </select>
              <div class="valid-feedback">
                ¡Bien!
              </div>
              <div class="invalid-feedback">
                Campo requerido.
              </div>
            </div>
            <div class="form-group">
              <label for="city" class="font-weight-bold">Ciudad*</label>
              <select class="custom-select mb-0" id="city" required v-model="contact.city">
                <option value="" v-if="!contact.state">Medellín</option>
                <option v-for="city in states[contact.state]" :value="city" :key="city">
                  {{ city }}
                </option>
              </select>
              <div class="valid-feedback">
                ¡Bien!
              </div>
              <div class="invalid-feedback">
                Campo requerido.
              </div>
            </div>
            <div class="form-group">
              <label for="name" class="font-weight-bold">Nombre*</label>
              <input type="text" class="form-control" id="name" placeholder="Pepito de Jesús"
                     maxlength="50" required v-model="contact.name">
              <div class="valid-feedback">
                ¡Bien!
              </div>
              <div class="invalid-feedback">
                Campo requerido.
              </div>
            </div>
            <div class="form-group">
              <label for="email" class="font-weight-bold">Correo*</label>
              <input type="email" class="form-control" id="email" placeholder="Pepitodejesus@gmail.com" required
                     maxlength="30" v-model="contact.email">
              <div class="valid-feedback">
                ¡Bien!
              </div>
              <div class="invalid-feedback">
                Campo requerido
              </div>
            </div>
            <button type="submit" class="btn mx-auto d-block rounded-pill text-white font-weight-bold">
              ENVIAR
            </button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import gql from 'graphql-tag'

export default {
  name: 'App',

  methods: {
    submit($event) {
      this.wasValidated = true
      if ($event.target.checkValidity()) {
        this.$apollo.mutate({
          mutation: gql`mutation($name: String!, $email: String!, $city: String!, $state: String!) {
            register (name: $name, email: $email, city: $city, state: $state) {
                contact { name }
            }
          }`,
          variables: this.contact,
          update:(store, {data}) => {
            console.log(data)
          }
        })
      }
    }
  },

  data: () => ({
    contact: {state: '', city: '', name: '', email: ''},
    wasValidated: false,

    // Can't get resources from the provided endpoint because of CORS policy restriction
    // Therefore, states and cities were manually extracted
    states: {
      "Amazonas": ["Leticia", "El encanto", "La Chorrera", "La Pedrera", "Miritiparaná", "Puerto Alegría", "Puerto Arica", "Puerto Nariño", "Puerto Santader"],
      "Atlántico": ["Baranoa", "Baranoa", "Barranquilla", "Campo de la Cruz", "Candelaría", "Galapa", "San Juan de Acosta", "Luruaco", "Malambo", "Manatí", "Palmar de Varela", "Piojo", "Polo Nuevo", "Ponedera", "Puerto Colombia", "Repelón", "Sabanagrande", "Sabanalarga", "Santa Lucía", "Santo Tomás", "Soledad", "Suan", "Tubara", "Usiacurí"],
      "Caquetá": ["Albania", "Belén de los Andaquíes", "Cartagena del Chaira", "Curillo", "El Doncello", "El Paujil", "Florencia", "La Montañita", "Milan", "Morelia", "Puerto Rico", "San José de Fragua", "San Vicente del Caguán", "Solano", "Solita", "Valparaíso"],
      "Cesar": ["Aguachica", "Agustín Codazzi", "Astrea", "Becerril", "Bosconia", "Chimichagua", "Chiriguaná", "Curumaní", "El Copey", "El Paso", "Gamarra", "González", "La Gloria", "La Jagua", "Ibirico", "Manaure", "Pailitas", "Pelaya", "Pueblo Bello", "Río de Oro", "Robles la Paz", "San Alberto", "San Diego", "San Martín", "Tamalameque", "Valledupar"],
      "Chocó": ["Acandi", "Alto Baudo", "Atrato", "Bagado", "Bahía Solano", "Belén de bajirá", "Bajo Baudo", "Bojayá", "Cantón de San Pablo", "Carmen del Darién", "Certeguí", "Condoto", "El Carmen", "Istmina", "Jurado", "Litoral del San Juan", "Lloró", "Medio Atrato", "Medio Baudo", "Medio San Juan", "Novita", "Nuquí", "Quibdó", "Río Iro", "Río Quito", "Riosucio", "San José del Palmar", "Sipí", "Tado", "Unguía", "Unión Panamericana"],
      "Córdoba": ["Ayapel", "Buenavista", "Canalete", "Cerete", "Chima", "Chinu", "Ciénaga de Oro", "Cotorra", "La Apartada", "Lorica", "Los Córdobas", "Momil", "Moñitos", "Montelibano", "Montería", "Planeta Rica", "Pueblo Nuevo", "Puerto Escondido", "Puerto Libertador", "Purísima", "Sahagun", "San Andrés", "Sotavento", "San Antero", "San Bernardo Viento", "San Carlos", "San Pelayo", "Tierralta", "Tuchin", "Valencia"],
      "Guainía": ["Inírida", "Barranco Minas", "Cacahual", "La Guadalupe", "Mapiripana", "Morichal", "Pana Pana", "Puerto Colombia", "San Felipe"],
      "Guaviare": ["Calamar", "El Retorno", "Miraflores", "San José del Guaviare"],
      "Huila": ["Acevedo", "Agrado", "Aipe", "Algeciras", "Altamira", "Baraya", "Campoalegre", "Colombia", "Elias", "Garzón", "Gigante", "Guadalupe", "Hobo", "Íquira", "Isnos", "La Argentina", "La Plata", "Nataga", "Neiva", "Oporapa", "Paicol", "Palermo", "Palestina", "Pital", "Pitalito", "Rivera", "Saladoblanco", "San Agustín", "Santa María", "Suaza", "Tarqui", "Tello", "Teruel", "Tesalia", "Timana", "Villavieja", "Yaguará"],
      "La Guajira": ["Riohacha", "Albania", "Barranca", "Dibulla", "Distracción", "El Molino", "Fonseca", "La Jagua del Pilar", "Maicao", "Manaure", "San Juan del Cesar", "Urumita", "Villa Nueva"],
      "Putumayo": ["Colón", "Mocoa", "Orito", "Puerto Asís", "Puerto Caicedo", "Puerto Guzman", "Leguizamo", "San Francisco", "San Miguel", "Santiago", "Sibundoy", "Valle del Guamuez", "Villagarzón"],
      "Quindío": ["Armenia", "Buenavista", "Calarca", "Circasia", "Córdoba", "Filandia", "Genova", "La Tebaida", "Montenegro", "Pijao", "Quimbaya", "Salento"],
      "San Andrés y Providencia": ["Providencia", "San Andrés y Providencia"],
      "Sucre": ["Buenavista", "Caimito", "Chalán", "Colosó", "Coveñas", "Corozal", "El Roble", "Galeras", "Guaranda", "La Unión", "Los Palmitos", "Majagual", "Morroa", "Ovejas", "Palmito", "Sampués", "San Benito Abad", "San Juan de Betulia", "San Marcos", "San Onofre", "San Pedro", "Sincé", "Sincelejo", "Sucre", "Tolú", "Toluviejo"],
      "Tolima": ["Alpujarra", "Alvarado", "Ambalema", "Anzoátegui", "Ataco", "Cajamarca", "Carmen de Apicalá", "Casabianca", "Chaparral", "Coello", "Coyaima", "Cunday", "Dolores", "Espinal", "Falán", "Flandes", "Fresno", "Guamo", "Guayabal", "Herveo", "Honda", "Ibagué", "Icononzo", "Lérida", "Líbano", "Mariquita", "Melgar", "Murillo", "Natagaima", "Ortega", "Palocabildo", "Piedras", "Planadas", "Prado", "Purificación", "Rioblanco", "Roncesvalles", "Rovira", "Saldaña", "San Antonio", "San Luis", "Santa Isabel", "Suárez", "Valle de San Juan", "Venadillo", "Villahermosa", "Villarrica"],
      "Vaupés": ["Cacarú", "Mitú", "Papunaua", "Pacoa", "Taraira", "Yavaraté"],
      "Vichada": ["Cumaribó", "La Primavera", "Puerto Carreño", "Santa Rosalia"]
    }
  }),
}
</script>

<style>
#app {
  font-family: "Roboto", serif;
  text-align: center;
  margin-top: 46px;
}

h1 {
  color: black;
  font-size: 2em !important;
  letter-spacing: -1px;
  margin-top: 34px !important;
}

#text {
  line-height: 1.2;
  color: #737172;
  margin-top: 27px;
  width: 707px;
  font-size: 1.08em;
}

#container {
  margin-top: 43px;
  margin-bottom: 100px;
}

#image {
  float: right;
  margin: 45px -5px 0 0;
}

form {
  text-align: left;
  padding: 50px 40px !important;
  box-shadow: 0 4px 13px #d0d0d0;
  width: 436px;
  border-radius: 10px 20px 20px 20px;
  margin-left: 8px;
}

.form-group {
  color: #727071 !important;
  margin-bottom: 23px !important;
}

label {
  color: black;
}

[type=submit] {
  background-color: #e03b65 !important;
  width: 132px;
  height: 50px;
  letter-spacing: 1px;
  margin-bottom: 0;
}

@media (max-width: 991px) {
  #image {
    float: none;
    margin-top: 0;
  }

  #text {
    width: 90%;
  }

  form {
    margin: 50px auto;
  }

  br {
    display: none;
  }
}
</style>
