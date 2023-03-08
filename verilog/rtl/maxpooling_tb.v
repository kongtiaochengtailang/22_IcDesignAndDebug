`timescale 1ns / 1ns

module maxpooling_tb();
	
	reg clk;
	reg rstn;
	reg ivalid;
	reg state;
	reg [7:0] din;
	

	wire[7:0] dout;
	wire ovalid;
	
	integer STATE = 0; 
	reg[10:0] cnt_line;
	integer count_w,fp_i;
	
	reg [7:0] pool_result_tb [0:150];
	reg [10:0] cnt_pool;
	

	maxpooling u_maxpooling(
	.clk(clk),
	.rstn(rstn),
	.ivalid(ivalid),
	.state(state),
	.din(din),
	.dout(dout),
	.ovalid(ovalid)
	);
	

	initial
	begin
		clk = 0;
		rstn = 0; 
		cnt_line = 0; 
		cnt_pool = 0;
		state = STATE;
		ivalid = 0; 
		din = 0;
		# 20;
		rstn = 1;
		ivalid = 1;
	end
	
	initial
	begin
		fp_i = $fopen("/home/vlsi/code/rtl/0.txt","r");
	end
	
	

	always@(posedge clk)
	begin
		if(ivalid == 1)
		begin
			count_w  <= $fscanf(fp_i,"%b" ,din);
			cnt_line <= cnt_line + 1;
			if(cnt_line == 10'd576) $display("picture read over");
			// $display("%d,%b",count_w,image_in);
		end
	end
	
	always #10 clk <= ~clk; 
	

	integer i;
	integer display_line = 0;
	always@(posedge clk)
	begin
		if(ovalid && cnt_pool<144) 
		begin
			pool_result_tb[cnt_pool] =  dout; 
			cnt_pool = cnt_pool + 1;
		end
	end
	
	initial
	begin
		# (11540+20); 
		
		$display("maxpooling complete");
		if(state == 0)
		begin
			for(i=0;i<144;i=i+1)
			begin 
				if(i == 0) $write("%d :", display_line);
				$write("%d ", pool_result_tb[i]); 
				//$write("i:%d %d ", i,pool_result_tb[i]);¡Œ
				if((i+1)%12 == 0)
				begin
					$display(" "); 
					display_line = display_line + 1;
					$write("%d :", display_line);
				end
			end	
		end
		else if(state == 1)
		begin
			for(i=0;i<16;i=i+1)
			begin
				$display("%d", pool_result_tb[i]);
			end	
		end
		
		$finish;
	end
	
endmodule
