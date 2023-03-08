`timescale 1ns / 1ns

module conv_tb();
	reg clk;
	reg rstn;
	reg start_conv;
	reg weight_en;
	reg [7:0] weight_c;
	reg state;
	
	reg start_window;
	reg [7:0] image_in;
	wire[31:0]conv_result;
	wire conv_ovalid;
	wire conv_done;
	
	wire [39:0] taps;
	
	parameter cycle = 20;
	
	integer fp_i;
	integer count_w;
	
	integer STATE = 0;
	
	reg[10:0] cnt_line;
	
	reg [31:0] conv_result_r [0:599];
	reg [10:0] cnt_conv; 
	
	always #10 clk <= ~clk;
	
	window window_inst(
		.clk  (clk),
		.rstn (rstn),
		.start(start_window),
		.state(state),
		.din  (image_in),
		.taps (taps)
	);
	

	conv u_conv(
		.clk(clk),
		.rstn(rstn),
		.start(start_conv),
		.weight_en(weight_en),
		.weight(weight_c),
		.taps(taps),
		.state(state),
		.dout(conv_result),
		.ovalid(conv_ovalid),
		.done(conv_done)
		);

	initial
	begin
		clk = 0;
		rstn = 0;
		state = STATE;
		cnt_conv = 0;
		# 20;
		rstn = 1;
		start_conv = 1;
		weight_en  = 1;
		weight_c = 8'd2;
	end
	
	initial
	begin
		cnt_line = 0;
		start_window = 0;
		# (20 + 10*cycle);
		start_window = 1; 
	end
	

	initial
	begin
		fp_i = $fopen("C:/Users/liuzhouquan/Desktop/num3_0.txt","r");
	end
	
	
	always@(posedge clk)
	begin
		if(start_window == 1)
		begin
			count_w  <= $fscanf(fp_i,"%b" ,image_in);
			cnt_line <= cnt_line + 1;
			if(cnt_line == 11'd784) $display("picture read over");
			// $display("%d,%b",count_w,image_in);
		end
	end
	
	
	integer i;
	integer display_line = 0;
	always@(posedge clk)
	begin
		if(conv_ovalid && !conv_done)
		begin
			//$display("cnt_conv: %d  ", cnt_conv);
			conv_result_r[cnt_conv] =  conv_result; 
			cnt_conv = cnt_conv + 1;
		end
		else 
		begin
			if(conv_done)
			begin
				conv_result_r[cnt_conv] =  conv_result;
				//$display("cnt_conv: %d  ", cnt_conv);
				$display("conv complete");
				if(state == 0)
				begin
					for(i=0;i<576;i=i+1)
					begin 
						if(i == 0) $write("%d :", display_line);
						
						$write("%d ", conv_result_r[i]);
						
						if((i+1)%24 == 0)
						begin
							$display(" ");
							display_line = display_line + 1;
							$write("%d :", display_line);
						end
					end	
				end
				else if(state == 1)
				begin
					for(i=0;i<64;i=i+1)
					begin
						$display("%d", conv_result_r[i]);
					end	
				end
				
			end
		end
	end

integer iIndex = 0;
integer iBmpWidth;
integer iBmpHight;
integer iBmpSize;
integer iDataStartIndex;
integer iBmpFileId;
integer iCode;
integer oBmpFileId_1;
reg [7:0] rBmpData [0:2000];

reg [7:0] conv_pixel_data_1 [0:2000];

reg [7:0] conv_BmpData_1 [0:2000];


initial 
begin
	iBmpFileId = $fopen("C:/Users/liuzhouquan/Desktop/3.bmp","rb");
	iCode = $fread(rBmpData, iBmpFileId);
	iBmpWidth 		= {rBmpData[21], rBmpData[20], rBmpData[19], rBmpData[18]};
	iBmpHight 		= {rBmpData[25], rBmpData[24], rBmpData[23], rBmpData[22]};
	iBmpSize  		= {rBmpData[ 5], rBmpData[ 4], rBmpData[ 3], rBmpData[ 2]};
	iDataStartIndex = {rBmpData[13], rBmpData[12], rBmpData[11], rBmpData[10]};
	$fclose(iBmpFileId);
	

	oBmpFileId_1 = $fopen("C:/Users/liuzhouquan/Desktop/test.bmp","wb+"); 
	#16700;
	
	for(iIndex = 0; iIndex < iBmpSize; iIndex = iIndex + 1) begin
		if(iIndex < 54)
			conv_BmpData_1[iIndex] = rBmpData[iIndex];
		else
			conv_BmpData_1[iIndex] = conv_pixel_data_1[iIndex-54];
	end	

	for (iIndex = 0; iIndex < iBmpSize; iIndex = iIndex + 1) begin
		$fwrite(oBmpFileId_1, "%c" , conv_BmpData_1[iIndex]);
	end
	
	$fclose(oBmpFileId_1);
end

integer k;
always@(posedge clk)
begin
	if(cnt_conv == 575) begin
		for(k=0;k<576;k=k+1) 
		begin
			conv_pixel_data_1[k*3]   <= conv_result_r[k];
			conv_pixel_data_1[k*3+1] <= conv_result_r[k];
			conv_pixel_data_1[k*3+2] <= conv_result_r[k];
		end
	end
end

endmodule
