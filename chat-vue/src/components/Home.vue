<template>
	<div>
		<h1> Chat use VueJS</h1>
		<button v-if='!auth' @click='goLogin'>Вход</button>
		<button v-else  @click='logout'>Выход</button>
		<Room v-if="auth" @openDialog="openDialog"></Room>
		<Dialog v-if='dialog.show' :id="dialog.id"></Dialog>
	</div>
</template>

<script>
	import Room from "@/components/rooms/Room.vue"
	import Dialog from "@/components/rooms/Dialog"
	export default {
		name: 'Home',
		components:{
			Room,
			Dialog
		},
		data(){
			return{
				dialog:{
					id:'',
					show: false,
				}
			}
		},
		computed:{
			auth(){
				if(sessionStorage.getItem("auth_token")){
					return true
				}
			}
		},
		methods: {
			goLogin(){
				this.$router.push({name:"Login"})
			},
			logout(){
				sessionStorage.removeItem("auth_token")
				window.location='/'
			},
			openDialog(id){
				this.dialog.id=id+1
				this.dialog.show=true
			}
		}
	}
</script>

<style>

</style>
