`timescale 1ns / 1ns



module fc_tb();
	reg clk;
	reg rstn;
	reg ivalid;
	reg signed [7:0] din_0;
	reg signed [7:0] din_1;
	reg signed [7:0] din_2;
	reg signed [7:0] din_3;
	reg signed [7:0] din_4;
	reg signed [7:0] din_5;
	reg signed [7:0] weight;
	reg weight_en;
	wire ovalid;
	wire signed [31:0]dout;
	
	reg[10:0] cnt_line; 
	integer count_w,fp_i;
	
	integer i_fc;
	
	reg signed[31:0] fc_result_tb ;
	reg [10:0] cnt_fc;
	
	fc u_fc(
		.clk(clk),
		.rstn(rstn),
		.ivalid(ivalid),
		.din_0(din_0),
		.din_1(din_1),
		.din_2(din_2),
		.din_3(din_3),
		.din_4(din_4),
		.din_5(din_5),
		.weight(weight),
		.weight_en(weight_en),
		.ovalid(ovalid),
		.dout(dout)
	);
	
	initial
	begin
		clk = 0;
		rstn = 0;
		cnt_line = 0; 
		cnt_fc = 0; 
		ivalid = 0; 
		din_0 = 0;
		din_1 = 0;
		din_2 = 0;
		din_3 = 0;
		din_4 = 0;
		din_5 = 0;
		weight_en = 0;
		weight = 0;
		# 20;
		rstn = 1;
		weight_en = 1;
		weight = 1;
		# (192*20);

		for(i_fc=0;i_fc<32;i_fc=i_fc+1)
		begin
			ivalid = 1;
			#20;
			ivalid = 0;
			#20;
		end
		
	end
	

	initial
	begin
		fp_i = $fopen("C:/Users/liuzhouquan/Desktop/1.txt","r");
	end
	
	

	always@(posedge clk)
	begin
		if(ivalid == 1)
		begin
			count_w  <= $fscanf(fp_i,"%b" ,din_0);
			count_w  <= $fscanf(fp_i,"%b" ,din_1);
			count_w  <= $fscanf(fp_i,"%b" ,din_2);
			count_w  <= $fscanf(fp_i,"%b" ,din_3);
			count_w  <= $fscanf(fp_i,"%b" ,din_4);
			count_w  <= $fscanf(fp_i,"%b" ,din_5);
			cnt_line <= cnt_line + 6;
			if(cnt_line == 9'd192) $display("picture read over");
			// $display("%d,%b",count_w,image_in);
		end
	end
	

	always #10 clk <= ~clk; 
	

	integer i;
	integer display_line = 0;
	always@(posedge clk)
	begin
		if(ovalid) 
		begin
			$display("cnt_fc: %d  ", cnt_fc);
			fc_result_tb[cnt_fc] =  dout; 
			$display("fc_result_tb: %d  ", dout);
			cnt_fc = cnt_fc + 1;
		end
	end

	initial
	begin
		# (20+192*20+32*40+5*20);
		
		$finish;
	end
endmodule
