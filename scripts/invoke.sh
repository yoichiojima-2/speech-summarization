#!/bin/bash

mkdir -p ./logs

input_directory="./data/input"

target=(
  "3_ad_tech_and_digital_marketing_10_app_marketing_1.aif"
  "3_ad_tech_and_digital_marketing_10_app_marketing_2.aif"
  "3_ad_tech_and_digital_marketing_10_app_marketing_3.aif"
  "3_ad_tech_and_digital_marketing_1_basic_and_trend_1.aif"
  "3_ad_tech_and_digital_marketing_1_basic_and_trend_2.aif"
  "3_ad_tech_and_digital_marketing_2_web_ad_1.aif"
  "3_ad_tech_and_digital_marketing_2_web_ad_2.aif"
  "3_ad_tech_and_digital_marketing_3_dmp_1.aif"
  "3_ad_tech_and_digital_marketing_4_dsp_1.aif"
  "3_ad_tech_and_digital_marketing_5_dentsu_digital_marketing_1.aif"
  "3_ad_tech_and_digital_marketing_5_dentsu_digital_marketing_2.aif"
  "3_ad_tech_and_digital_marketing_5_dentsu_digital_marketing_3.aif"
  "3_ad_tech_and_digital_marketing_5_dentsu_digital_marketing_4.aif"
  "3_ad_tech_and_digital_marketing_5_dentsu_digital_marketing_5.aif"
  "3_ad_tech_and_digital_marketing_5_dentsu_digital_marketing_6.aif"
  "3_ad_tech_and_digital_marketing_6_movie_marketing_1.aif"
  "3_ad_tech_and_digital_marketing_6_movie_marketing_2.aif"
  "3_ad_tech_and_digital_marketing_7_instagram_marketing_1.aif"
  "3_ad_tech_and_digital_marketing_7_instagram_marketing_2.aif"
  "3_ad_tech_and_digital_marketing_7_instagram_marketing_3.aif"
  "3_ad_tech_and_digital_marketing_7_instagram_marketing_4.aif"
  "3_ad_tech_and_digital_marketing_7_instagram_marketing_5.aif"
  "3_ad_tech_and_digital_marketing_8_twitter_marketing_1.aif"
  "3_ad_tech_and_digital_marketing_8_twitter_marketing_2.aif"
  "3_ad_tech_and_digital_marketing_9_line_marketing_1.aif"
  "3_ad_tech_and_digital_marketing_9_line_marketing_2.aif"
  "5_marketing_strategy_10_behavioral_economics_1.aif"
  "5_marketing_strategy_10_behavioral_economics_2.aif"
  "5_marketing_strategy_10_behavioral_economics_3.aif"
  "5_marketing_strategy_10_behavioral_economics_4.aif"
  "5_marketing_strategy_10_behavioral_economics_5.aif"
  "5_marketing_strategy_10_behavioral_economics_6.aif"
  "5_marketing_strategy_1_digital_marketing_intro_1.aif"
  "5_marketing_strategy_1_digital_marketing_intro_2.aif"
  "5_marketing_strategy_1_digital_marketing_intro_3.aif"
  "5_marketing_strategy_6_standard_of_digital_marketing_1.aif"
  "5_marketing_strategy_8_marketing_thing_out_of_box_1.aif"
  "5_marketing_strategy_8_marketing_thing_out_of_box_2.aif"
  "5_marketing_strategy_8_marketing_thing_out_of_box_3.aif"
  "5_marketing_strategy_8_marketing_thing_out_of_box_4.aif"
  "1_presentation_1_making_slide_1.aif"
  "1_presentation_1_making_slide_2.aif"
  "1_presentation_3_excel_1.aif"
  "1_presentation_3_excel_2.aif"
  "1_presentation_3_excel_3.aif"
  "1_presentation_3_excel_4.aif"
  "1_presentation_3_excel_5.aif"
  "1_presentation_3_excel_6.aif"
  "1_presentation_4_next_gen_slides_1.aif"
  "1_presentation_4_next_gen_slides_2.aif"
  "1_presentation_5_design_1.aif"
  "1_presentation_5_design_2.aif"
  "1_presentation_5_design_3.aif"
  "1_presentation_5_design_4.aif"
  "1_presentation_6_logical_talking_1.aif"
  "1_presentation_6_logical_talking_2.aif"
  "1_presentation_6_logical_talking_3.aif"
  "1_presentation_6_logical_talking_4.aif"
  "1_presentation_6_logical_talking_5.aif"
  "1_presentation_6_logical_talking_6.aif"
  "1_presentation_7_making_content_1.aif"
  "1_presentation_7_making_content_2.aif"
  "1_presentation_7_making_content_3.aif"
  "2_digital_reskilling_1_know_digital_1.aif"
  "2_digital_reskilling_1_know_digital_2.aif"
  "2_digital_reskilling_1_know_digital_3.aif"
  "2_digital_reskilling_1_know_digital_4.aif"
  "2_digital_reskilling_1_know_digital_5.aif"
  "2_digital_reskilling_1_know_digital_6.aif"
  "2_digital_reskilling_2_touching_tools_1.aif"
  "2_digital_reskilling_2_touching_tools_10.aif"
  "2_digital_reskilling_2_touching_tools_11.aif"
  "2_digital_reskilling_2_touching_tools_12.aif"
  "2_digital_reskilling_2_touching_tools_13.aif"
  "2_digital_reskilling_2_touching_tools_14.aif"
  "2_digital_reskilling_2_touching_tools_15.aif"
  "2_digital_reskilling_2_touching_tools_16.aif"
  "2_digital_reskilling_2_touching_tools_17.aif"
  "2_digital_reskilling_2_touching_tools_18.aif"
  "2_digital_reskilling_2_touching_tools_19.aif"
  "2_digital_reskilling_2_touching_tools_2.aif"
  "2_digital_reskilling_2_touching_tools_20.aif"
  "2_digital_reskilling_2_touching_tools_21.aif"
  "2_digital_reskilling_2_touching_tools_22.aif"
  "2_digital_reskilling_2_touching_tools_23.aif"
  "2_digital_reskilling_2_touching_tools_24.aif"
  "2_digital_reskilling_2_touching_tools_25.aif"
  "2_digital_reskilling_2_touching_tools_3.aif"
  "2_digital_reskilling_2_touching_tools_4.aif"
  "2_digital_reskilling_2_touching_tools_5.aif"
  "2_digital_reskilling_2_touching_tools_6.aif"
  "2_digital_reskilling_2_touching_tools_7.aif"
  "2_digital_reskilling_2_touching_tools_8.aif"
  "2_digital_reskilling_2_touching_tools_9.aif"
  "2_digital_reskilling_3_building_system_10.aif"
  "2_digital_reskilling_3_building_system_11.aif"
  "2_digital_reskilling_3_building_system_12.aif"
  "2_digital_reskilling_3_building_system_2.aif"
  "2_digital_reskilling_3_building_system_3.aif"
  "2_digital_reskilling_3_building_system_4.aif"
  "2_digital_reskilling_3_building_system_5.aif"
  "2_digital_reskilling_3_building_system_6.aif"
  "2_digital_reskilling_3_building_system_7.aif"
  "2_digital_reskilling_3_building_system_8.aif"
  "2_digital_reskilling_3_building_system_9.aif"
  "4_marketing_1_open_campus_1.aif"
  "4_marketing_2_4_marketing_basic_1.aif"
  "4_marketing_2_4_marketing_basic_10.aif"
  "4_marketing_2_4_marketing_basic_11.aif"
  "4_marketing_2_4_marketing_basic_12.aif"
  "4_marketing_2_4_marketing_basic_2.aif"
  "4_marketing_2_4_marketing_basic_3.aif"
  "4_marketing_2_4_marketing_basic_4.aif"
  "4_marketing_2_4_marketing_basic_5.aif"
  "4_marketing_2_4_marketing_basic_6.aif"
  "4_marketing_2_4_marketing_basic_7.aif"
  "4_marketing_2_4_marketing_basic_8.aif"
  "4_marketing_2_4_marketing_basic_9.aif"
  "4_marketing_3_digital_4_marketing_basic_1.aif"
  "4_marketing_3_digital_4_marketing_basic_2.aif"
  "4_marketing_3_digital_4_marketing_basic_3.aif"
  "4_marketing_3_digital_4_marketing_basic_4.aif"
  "4_marketing_3_digital_4_marketing_basic_5.aif"
  "4_marketing_3_digital_4_marketing_basic_6.aif"
  "4_marketing_3_digital_4_marketing_basic_7.aif"
  "4_marketing_3_digital_4_marketing_basic_8.aif"
  "4_marketing_4_4_marketing_in_practice_1.aif"
  "4_marketing_4_4_marketing_in_practice_2.aif"
  "4_marketing_4_4_marketing_in_practice_3.aif"
)

for file in "${target[@]}"; do
  filename_wo_ext="${file%.*}"
  echo "Processing ${input_directory}/${file}"
  echo "${input_directory}/${file}"
  poetry run python \
    ./speech_summarization/pipeline.py MergeText \
    --target "${input_directory}/${file}" \
    | tee "./logs/${filename_wo_ext}.log" 2>&1
done
