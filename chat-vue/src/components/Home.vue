<template>
	<mu-container>
		<mu-appbar style="width: 100%;" color="primary" xl='10'>
  			Chat use VueJS
  			<mu-button v-if='!auth' @click='goLogin'flat slot="right">LOGIN</mu-button>
  			<mu-button v-else  @click='logout' flat slot="right">OUTLOG</mu-button>
		</mu-appbar>
		<mu-row>
			
		</mu-row>
		<mu-row>
			<Room v-if="auth" @openDialog="openDialog"></Room>
			<Dialog v-if='dialog.show' :id="dialog.id"></Dialog>
		</mu-row>
	</mu-container>
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
				this.dialog.id=id
				this.dialog.show=true
			}
		}
	}
</script>

<style>

</style>
