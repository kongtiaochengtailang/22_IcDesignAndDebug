module maxpooling
(
    input  clk,
    input  rstn,
    input  ivalid, // input valid,      
    input  state, // 0: 24*24, 1: 12*12
    input  [7:0] din,   
    output ovalid,      
    output [7:0] dout    
);

	reg [7:0] data [0:23];  
	reg [6:0] ptr; // to point number's address         
	reg cnt; //output                 
	reg [7:0] data_reg_0;   
	reg [7:0] data_reg_1;   
	reg [7:0] dout_r;
	

	always@(posedge clk)begin
		if(!rstn)
			ptr <= 7'b0000000;
		else
			case(state)
				1'b0:begin
					if(ptr == 7'd48-1) 
						ptr <= 7'd0;
					else 
						if(!ivalid)
							ptr <= ptr;
						else
							ptr <= ptr + 7'd1;
					end
				1'b1:begin
					if(ptr == 7'd16-1)
						ptr <= 7'd0;
					else 
						if(!ivalid)
							ptr <= ptr;
						else
							ptr <= ptr + 7'd1;
					end               
			endcase
	end
	

	always@(posedge clk or negedge rstn)begin
	if(!rstn)
		cnt <= 0;
	else
		case(state)
			1'b0:begin
					if(ptr < 7'd25 - 1)
						cnt <= 0;
					else
						if(ivalid)
							cnt <= cnt + 1'b1;
						else
							cnt <= cnt;
				end
			1'b1:begin
					if(ptr <= 7'd7)
						cnt <= 0;
					else
						if(ivalid)
							cnt <= cnt + 1'b1;
						else
							cnt <= cnt;
				end
		endcase
	end
	
	always@(posedge clk)
	begin
		case(state)
		1'b0:begin
			if(ptr <= 7'd24 && ivalid) 
				data[ptr] <= din;
			end
		1'b1:begin
			if(ptr <= 7'd8 && ivalid) 
				data[ptr] <= din;
			end          
		endcase   
	end

	always@(posedge clk)
	begin
		case({state,cnt})
		2'b00:begin
			if(ptr >= 7'd24)
			begin
				if(din>data[ptr-7'd24])
					data_reg_0 <= din;
				else
					data_reg_0 <= data[ptr-7'd24];
			end
			else
				data_reg_0 <= 0;
			end
		2'b01:begin
			if(ptr >= 7'd24)
			begin
				if(din>data[ptr-7'd24])
					data_reg_1 <= din;
				else
					data_reg_1 <= data[ptr-7'd24];
			end
			else
				data_reg_1 <= 0;
			end
		2'b10:begin
			if(ptr >= 7'd9)
			begin
				if(din>data[ptr-7'd9])
					data_reg_0 <= din;
				else
					data_reg_0 <= data[ptr-7'd9];
			end
			else
				data_reg_0 <= 0;
			end
		2'b11:begin
			if(ptr >= 7'd9)
			begin
				if(din>data[ptr-7'd9])
					data_reg_1 <= din;
				else
					data_reg_1 <= data[ptr-7'd9];
			end
			else
				data_reg_1 <= 0;
			end 
		default:begin
				data_reg_1 <= 0; 
				data_reg_0 <= 0;
				end         
		endcase
	end


	reg cnt_d;
	always@(posedge clk)begin
		if(!rstn)
			cnt_d <= 0;
		else
			cnt_d <= cnt;
	end
	

	assign ovalid = ~cnt && cnt_d; // output is valid only after 4 numbers have been calculated
	assign dout   = data_reg_1 > data_reg_0 ? data_reg_1 : data_reg_0;
	
endmodule
