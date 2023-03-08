`timescale 1ns / 1ps


module window_tb();
	reg clk;
	reg resetn;
	reg start_window;
	reg state;
	reg[7:0] image_in;
	wire[39:0] taps;
	
	integer fp_i;
	integer count_w;
	
	reg[10:0] cnt_line;
	
	window window_inst(
		.clk  (clk),
		.rstn (resetn),
		.start(start_window),
		.state(state),
		.din  (image_in),
		.taps (taps)
	);
	
	initial
	begin
		fp_i = $fopen("C:/Users/liuzhouquan/Desktop/cnn_accelerator-main/cnn_accelerator-main/sim/28x28/num3_0.txt","r");
		if (!fp_i) begin
		      $display("can not open sim_input.txt");
		      $finish;
		end
	end
	initial
	begin
		cnt_line = 0;
		clk = 0;
		start_window = 0;
		state = 0;
		# 20;
		start_window = 1;
	end
	
	always@(posedge clk)
	begin
		begin
			count_w  <= $fscanf(fp_i,"%b" ,image_in);
			cnt_line <= cnt_line + 1;
			if(cnt_line == 11'd784) $display("picture read over");
		end
	end
	
	always #10 clk <= ~clk; 
endmodule
