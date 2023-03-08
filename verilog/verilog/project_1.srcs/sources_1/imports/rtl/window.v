module window   
(
    input  clk,
    input  rstn,
    input  start,
    input  state,                   
    input  [7:0]  din,
    output [39:0] taps
);
           
	integer i;
	reg [7:0] mem [0:139];
	always@(posedge clk)begin
		if(start)
			begin
			   mem[0] <= din;           
			   for(i=0;i<139;i=i+1)  
			   	  mem[i+1] <= mem[i];
			end
	end
	assign taps = (!state)?{mem[139],mem[111],mem[83],mem[55],mem[27]}:{mem[59],mem[47],mem[35],mem[23],mem[11]};

endmodule



