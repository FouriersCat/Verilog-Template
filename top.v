`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2019/09/03 15:04:00
// Design Name: 
// Module Name: top
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: 
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////

module top(
 input  clk_n,
 input  clk_p,
 output [14:0]DDR3_addr,
 output [2:0]DDR3_ba,
 output DDR3_cas_n,
 output [0:0]DDR3_ck_n,
 output [0:0]DDR3_ck_p,
 output [0:0]DDR3_cke,
 output [0:0]DDR3_cs_n,
 output [7:0]DDR3_dm,
 inout  [63:0]DDR3_dq,
 inout  [7:0]DDR3_dqs_n,
 inout  [7:0]DDR3_dqs_p,
 output [0:0]DDR3_odt,
 output DDR3_ras_n,
 output DDR3_reset_n,
 output DDR3_we_n,
 input  [0:0]MB_INTC,
 input  ext_reset_in  
    );
    
 wire  AXI_CLK;
 reg  AXI_RSTN;
 reg [9:0] cnt;
 always @ ( posedge AXI_CLK )
 begin
    if(cnt<=10'd1000)
        cnt <= cnt + 1'b1;
 end
 
 always @ ( posedge AXI_CLK )
 begin
    if(cnt<=10'd500)
        AXI_RSTN <= 1'b0;
    else
        AXI_RSTN <= 1'b1;
 end    
 
  ddr_test_wrapper inst_ddr(
   .AXI_CLK         (AXI_CLK        ),
   .AXI_RSTN        (AXI_RSTN       ),
   .CLK_IN1_D_clk_n (clk_n          ),
   .CLK_IN1_D_clk_p (clk_p          ),
   .DDR3_addr       (DDR3_addr      ),
   .DDR3_ba         (DDR3_ba        ),
   .DDR3_cas_n      (DDR3_cas_n     ),
   .DDR3_ck_n       (DDR3_ck_n      ),
   .DDR3_ck_p       (DDR3_ck_p      ),
   .DDR3_cke        (DDR3_cke       ),
   .DDR3_cs_n       (DDR3_cs_n      ),
   .DDR3_dm         (DDR3_dm        ),
   .DDR3_dq         (DDR3_dq        ),
   .DDR3_dqs_n      (DDR3_dqs_n     ),
   .DDR3_dqs_p      (DDR3_dqs_p     ),
   .DDR3_odt        (DDR3_odt       ),
   .DDR3_ras_n      (DDR3_ras_n     ),
   .DDR3_reset_n    (DDR3_reset_n   ),
   .DDR3_we_n       (DDR3_we_n      ),
   .MB_INTC         (MB_INTC        ),
   .ext_reset_in    (ext_reset_in   ),
   .init_calib_complete(init_calib_complete),
   .mmcm_locked     (mmcm_locked),
   .sys_rst         (~AXI_RSTN),
   .ui_clk_sync_rst (ui_clk_sync_rst)
   );
     
    
endmodule
