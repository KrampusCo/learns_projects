<template>
	<mu-col span='8' xl='9' >
		<mu-container class="dialog">
			<mu-row v-for="dialog in dialogs"
			direction="column" 
			jestify-content="start" 
			align-items="end" 
			>
				<p><strong>{{dialog.user.username}}</strong></p>
				<p>{{dialog.text}}</p>
				<span>{{dialog.date}}</span>
			</mu-row>
		</mu-container>
		<mu-container>
			<mu-row>
				<mu-text-field multi-line :rows="2"  placeholder="InputText"></mu-text-field>	
  					<mu-button color="primary" class="btn-send" >Enter</mu-button>
				
			</mu-row>
		</mu-container>
	</mu-col>
	
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
				dialogs:'',
				form:{
					textarea:'',
				}
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
						room: this.id
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
.dialog{
border: 4px solid black;
width: 100%;
}
.btn-send{
	margin: 10px 0px 0px 10px;
}
</style>
