<template>
	<div>
		<div v-for="dialog in dialogs">

		<h2>{{dialog.user.username}}</h2>
		<p>{{dialog.text}}</p>
		<span>{{dialog.date}}</span>
		</div>
	</div>
</template>

<script>
	import $ from "jquery"

	export default{
		name:"Dialog",
		props:{
			id:'',
		},
		data(){
			return{
				dialogs:''
			}
		},
		created() {
			$.ajaxSetup({
				headers: {"Authorization": "Token " + sessionStorage.getItem("auth_token")},
			});
			this.loadDialog()
		},
		methods:{
			loadDialog(){
				$.ajax({
					url:"http://localhost:8000/api/v1/chat/dialog/",
					type:"GET",
					data:{
						room: this.id+1
					},
					success: (response) => {
						this.dialogs=response.data.data
					}

				})
			}
		}
	}
</script>

<style scoped>

</style>
