import psycopg2

# try:
#     connection = psycopg2.connect(host='st-writer-rds.advinow-dev.int',
#                                          database='oe2',
#                                          user='root',
#                                          password='aQfeW4D3')
try:
    connection = psycopg2.connect(host='ec2-50-16-108-254.compute-1.amazonaws.com',
                                         database='d9v89qak4p5fl8',
                                         user='rkjgpgunvofpws',
                                         password='03cb1ce45185cb70077acf3b73fc0b4bae1f17937b0058ce9fa62254472570ac')
# try:
#     connection = psycopg2.connect(host='localhost',
#                                          database='advi',
#                                          user='postgres',
#                                          password='BillGates94415')

    postgreSql_insert_query = """INSERT INTO treatment_treatmenttyperefmodel_treatment_type_desc (id, treatmenttyperefmodel_id, treatmenttyperefdesc_id) 
                           VALUES 
(1, 1, 334 ),
(2, 1, 413 ),
(3, 1, 414 ),
(4, 1, 415 ),
(5, 1, 416 ),
(6, 1, 417 ),
(7, 1, 418 ),
(8, 1, 419 ),
(9, 1, 420 ),
(10, 1, 421 ),
(11, 1, 422 ),
(12, 1, 423 ),
(13, 1, 424 ),
(14, 1, 425 ),
(15, 1, 461 ),
(16, 1, 663 ),
(17, 1, 664 ),
(18, 1, 665 ),
(19, 1, 666 ),
(20, 1, 667 ),
(21, 1, 668 ),
(22, 1, 669 ),
(23, 1, 670 ),
(24, 1, 671 ),
(25, 1, 672 ),
(26, 1, 673 ),
(27, 1, 674 ),
(28, 1, 675 ),
(29, 1, 676 ),
(30, 1, 677 ),
(31, 1, 678 ),
(32, 1, 679 ),
(33, 1, 680 ),
(34, 1, 681 ),
(35, 1, 682 ),
(36, 1, 683 ),
(37, 1, 684 ),
(38, 1, 685 ),
(39, 1, 686 ),
(40, 1, 687 ),
(41, 1, 688 ),
(42, 1, 689 ),
(43, 1, 692 ),
(44, 1, 693 ),
(45, 4, 5 ),
(46, 4, 75 ),
(47, 4, 76 ),
(48, 4, 77 ),
(49, 4, 80 ),
(50, 4, 115 ),
(51, 4, 447 ),
(52, 4, 448 ),
(53, 4, 462 ),
(54, 4, 463 ),
(55, 4, 464 ),
(56, 4, 465 ),
(57, 4, 466 ),
(58, 4, 467 ),
(59, 4, 468 ),
(60, 4, 469 ),
(61, 4, 470 ),
(62, 4, 471 ),
(63, 4, 626 ),
(64, 4, 631 ),
(65, 4, 707 ),
(66, 4, 712 ),
(67, 4, 765 ),
(68, 4, 773 ),
(69, 4, 786 ),
(70, 4, 450 ),
(71, 4, 474 ),
(72, 5, 2 ),
(73, 5, 58 ),
(74, 5, 59 ),
(75, 5, 336 ),
(76, 5, 338 ),
(77, 5, 449 ),
(78, 5, 450 ),
(79, 5, 451 ),
(80, 5, 452 ),
(81, 5, 453 ),
(82, 5, 454 ),
(83, 5, 455 ),
(84, 5, 456 ),
(85, 5, 636 ),
(86, 5, 703 ),
(87, 5, 70 ),
(88, 5, 709 ),
(89, 5, 710 ),
(90, 5, 713 ),
(91, 5, 715 ),
(92, 5, 721 ),
(93, 5, 799 ),
(94, 5, 806 ),
(95, 6, 71 ),
(96, 6, 457 ),
(97, 6, 458 ),
(98, 6, 745 ),
(99, 6, 748 ),
(100, 6, 749 ),
(101, 6, 758 ),
(102, 6, 768 ),
(103, 6, 776 ),
(104, 6, 778 ),
(105, 6, 787 ),
(106, 6, 788 ),
(107, 6, 798 ),
(108, 7, 6 ),
(109, 7, 10 ),
(110, 7, 12 ),
(111, 7, 39 ),
(112, 7, 40 ),
(113, 7, 57 ),
(114, 7, 67 ),
(115, 7, 78 ),
(116, 7, 81 ),
(117, 7, 83 ),
(118, 7, 337 ),
(119, 7, 390 ),
(120, 7, 459 ),
(121, 7, 460 ),
(122, 7, 472 ),
(123, 7, 473 ),
(124, 7, 474 ),
(125, 7, 475 ),
(126, 7, 476 ),
(127, 7, 615 ),
(128, 7, 635 ),
(129, 7, 644 ),
(130, 7, 708 ),
(131, 7, 711 ),
(132, 7, 718 ),
(133, 7, 719 ),
(134, 7, 720 ),
(135, 7, 703 ),
(136, 7, 731 ),
(137, 7, 738 ),
(138, 7, 741 ),
(139, 7, 742 ),
(140, 7, 750 ),
(141, 7, 753 ),
(142, 7, 754 ),
(143, 7, 755 ),
(144, 7, 756 ),
(145, 7, 774 ),
(146, 7, 775 ),
(147, 7, 782 ),
(148, 7, 783 ),
(149, 7, 793 ),
(150, 7, 794 ),
(151, 7, 795 ),
(152, 7, 809 ),
(153, 7, 812 ),
(154, 8, 324 ),
(155, 8, 477 ),
(156, 8, 478 ),
(157, 8, 479 ),
(158, 8, 480 ),
(159, 8, 481 ),
(160, 8, 482 ),
(161, 8, 483 ),
(162, 8, 484 ),
(163, 8, 485 ),
(164, 8, 486 ),
(165, 8, 487 ),
(166, 8, 488 ),
(167, 8, 645 ),
-- (168, 9, 328 ),
(169, 9, 329 ),
(170, 9, 330 ),
(171, 9, 331 ),
(172, 9, 332 ),
(173, 9, 333 ),
(174, 9, 489 ),
-- (175, 9, 328 ),
(176, 9, 491 ),
-- (177, 9, 330 ),
(178, 9, 474 ),
-- (179, 9, 331 ),
-- (180, 9, 332 ),
(181, 9, 760 ),
(182, 10, 73 ),
(183, 10, 85 ),
(184, 10, 86 ),
(185, 10, 88 ),
(186, 10, 96 ),
(187, 10, 118 ),
(188, 10, 119 ),
(189, 10, 120 ),
(190, 10, 121 ),
(191, 10, 122 ),
(192, 10, 123 ),
(193, 10, 124 ),
(194, 10, 125 ),
(195, 10, 126 ),
(196, 10, 127 ),
(197, 10, 128 ),
(198, 10, 129 ),
(199, 10, 130 ),
(200, 10, 131 ),
(201, 10, 132 ),
(202, 10, 133 ),
(203, 10, 134 ),
(204, 10, 135 ),
(205, 10, 136 ),
(206, 10, 137 ),
(207, 10, 138 ),
(208, 10, 139 ),
(209, 10, 140 ),
(210, 10, 141 ),
(211, 10, 142 ),
(212, 10, 143 ),
(213, 10, 144 ),
(214, 10, 145 ),
(215, 10, 146 ),
(216, 10, 147 ),
(217, 10, 148 ),
(218, 10, 149 ),
(219, 10, 150 ),
(220, 10, 151 ),
(221, 10, 152 ),
(222, 10, 153 ),
(223, 10, 340 ),
(224, 10, 341 ),
(225, 10, 342 ),
(226, 10, 343 ),
(227, 10, 344 ),
(228, 10, 345 ),
(229, 10, 346 ),
(230, 10, 347 ),
(231, 10, 348 ),
(232, 10, 349 ),
(233, 10, 350 ),
(234, 10, 351 ),
(235, 10, 352 ),
(236, 10, 353 ),
(237, 10, 354 ),
(238, 10, 355 ),
(239, 10, 356 ),
(240, 10, 357 ),
(241, 10, 358 ),
(242, 10, 359 ),
(243, 10, 360 ),
(244, 10, 361 ),
(245, 10, 362 ),
(246, 10, 363 ),
(247, 10, 364 ),
(248, 10, 365 ),
(249, 10, 366 ),
(250, 10, 367 ),
(251, 10, 368 ),
(252, 10, 369 ),
(253, 10, 370 ),
(254, 10, 371 ),
(255, 10, 372 ),
(256, 10, 373 ),
(257, 10, 374 ),
(258, 10, 375 ),
(259, 10, 376 ),
(260, 10, 377 ),
(261, 10, 378 ),
(262, 10, 379 ),
(263, 10, 380 ),
(264, 10, 381 ),
(265, 10, 382 ),
(266, 10, 383 ),
(267, 10, 384 ),
(268, 10, 385 ),
(269, 10, 386 ),
(270, 10, 387 ),
(271, 10, 388 ),
(272, 10, 389 ),
(273, 10, 391 ),
(274, 10, 392 ),
(275, 10, 445 ),
(276, 10, 446 ),
(277, 10, 496 ),
(278, 10, 497 ),
(279, 10, 498 ),
(280, 10, 499 ),
(281, 10, 500 ),
(282, 10, 501 ),
(283, 10, 502 ),
(284, 10, 503 ),
(285, 10, 504 ),
(286, 10, 505 ),
(287, 10, 506 ),
(288, 10, 507 ),
(289, 10, 474 ),
(290, 10, 509 ),
(291, 10, 510 ),
(292, 10, 511 ),
(293, 10, 512 ),
(294, 10, 513 ),
(295, 10, 514 ),
(296, 10, 515 ),
(297, 10, 516 ),
(298, 10, 616 ),
(299, 10, 642 ),
(300, 10, 650 ),
(301, 10, 651 ),
-- (302, 10, 651 ),
(303, 10, 697 ),
(304, 10, 698 ),
(305, 10, 699 ),
(306, 11, 1 ),
(307, 11, 3 ),
(308, 11, 14 ),
(309, 11, 17 ),
(310, 11, 18 ),
(311, 11, 19 ),
(312, 11, 20 ),
(313, 11, 23 ),
(314, 11, 24 ),
(315, 11, 27 ),
(316, 11, 28 ),
(317, 11, 33 ),
(318, 11, 34 ),
(319, 11, 35 ),
(320, 11, 154 ),
(321, 11, 155 ),
(322, 11, 156 ),
(323, 11, 157 ),
(324, 11, 158 ),
(325, 11, 159 ),
(326, 11, 160 ),
(327, 11, 161 ),
(328, 11, 162 ),
(329, 11, 163 ),
(330, 11, 164 ),
(331, 11, 165 ),
(332, 11, 166 ),
(333, 11, 167 ),
(334, 11, 168 ),
(335, 11, 169 ),
(336, 11, 170 ),
(337, 11, 171 ),
(338, 11, 172 ),
(339, 11, 173 ),
(340, 11, 174 ),
(341, 11, 175 ),
(342, 11, 176 ),
(343, 11, 177 ),
(344, 11, 178 ),
(345, 11, 179 ),
(346, 11, 180 ),
(347, 11, 181 ),
(348, 11, 182 ),
(349, 11, 183 ),
(350, 11, 184 ),
(351, 11, 185 ),
(352, 11, 186 ),
(353, 11, 187 ),
(354, 11, 188 ),
(355, 11, 189 ),
(356, 11, 190 ),
(357, 11, 191 ),
(358, 11, 192 ),
(359, 11, 193 ),
(360, 11, 194 ),
(361, 11, 195 ),
(362, 11, 196 ),
(363, 11, 197 ),
(364, 11, 198 ),
(365, 11, 199 ),
(366, 11, 200 ),
(367, 11, 201 ),
(368, 11, 202 ),
(369, 11, 203 ),
(370, 11, 204 ),
(371, 11, 205 ),
(372, 11, 206 ),
(373, 11, 207 ),
(374, 11, 208 ),
(375, 11, 209 ),
(376, 11, 210 ),
(377, 11, 211 ),
(378, 11, 212 ),
(379, 11, 213 ),
(380, 11, 214 ),
(381, 11, 215 ),
(382, 11, 216 ),
(383, 11, 217 ),
(384, 11, 218 ),
(385, 11, 219 ),
(386, 11, 220 ),
-- (387, 11, 221 ),
(388, 11, 222 ),
(389, 11, 223 ),
(390, 11, 224 ),
(391, 11, 225 ),
(392, 11, 226 ),
(393, 11, 227 ),
(394, 11, 228 ),
(395, 11, 229 ),
(396, 11, 230 ),
(397, 11, 231 ),
(398, 11, 232 ),
(399, 11, 233 ),
(400, 11, 234 ),
(401, 11, 235 ),
(402, 11, 236 ),
(403, 11, 237 ),
(404, 11, 238 ),
(405, 11, 239 ),
(406, 11, 240 ),
(407, 11, 241 ),
(408, 11, 242 ),
(409, 11, 243 ),
(410, 11, 244 ),
(411, 11, 245 ),
(412, 11, 246 ),
(413, 11, 247 ),
(414, 11, 248 ),
(415, 11, 249 ),
(416, 11, 250 ),
(417, 11, 251 ),
(418, 11, 252 ),
(419, 11, 253 ),
(420, 11, 254 ),
(421, 11, 255 ),
(422, 11, 256 ),
(423, 11, 257 ),
(424, 11, 258 ),
(425, 11, 259 ),
(426, 11, 260 ),
(427, 11, 261 ),
(428, 11, 262 ),
(429, 11, 263 ),
(430, 11, 264 ),
(431, 11, 265 ),
(432, 11, 266 ),
(433, 11, 267 ),
(434, 11, 268 ),
(435, 11, 269 ),
(436, 11, 270 ),
(437, 11, 271 ),
(438, 11, 272 ),
(439, 11, 273 ),
(440, 11, 274 ),
(441, 11, 275 ),
(442, 11, 276 ),
(443, 11, 277 ),
(444, 11, 278 ),
(445, 11, 279 ),
(446, 11, 280 ),
(447, 11, 281 ),
(448, 11, 282 ),
(449, 11, 283 ),
-- (450, 11, 284 ),
(451, 11, 285 ),
(452, 11, 286 ),
(453, 11, 287 ),
(454, 11, 288 ),
(455, 11, 289 ),
(456, 11, 290 ),
(457, 11, 291 ),
(458, 11, 292 ),
(459, 11, 293 ),
(460, 11, 294 ),
(461, 11, 295 ),
(462, 11, 296 ),
(463, 11, 297 ),
(464, 11, 298 ),
(465, 11, 299 ),
(466, 11, 300 ),
(467, 11, 301 ),
(468, 11, 302 ),
(469, 11, 303 ),
(470, 11, 304 ),
(471, 11, 305 ),
(472, 11, 306 ),
(473, 11, 307 ),
(474, 11, 308 ),
(475, 11, 309 ),
(476, 11, 310 ),
(477, 11, 311 ),
(478, 11, 312 ),
(479, 11, 313 ),
(480, 11, 314 ),
(481, 11, 315 ),
(482, 11, 316 ),
(483, 11, 393 ),
(484, 11, 394 ),
(485, 11, 395 ),
(486, 11, 396 ),
(487, 11, 397 ),
(488, 11, 398 ),
(489, 11, 399 ),
(490, 11, 400 ),
(491, 11, 401 ),
(492, 11, 402 ),
(493, 11, 403 ),
(494, 11, 404 ),
(495, 11, 405 ),
(496, 11, 406 ),
(497, 11, 407 ),
(498, 11, 408 ),
-- (499, 11, 409 ),
(500, 11, 410 ),
(501, 11, 411 ),
(502, 11, 412 ),
(503, 11, 517 ),
(504, 11, 518 ),
(505, 11, 519 ),
(506, 11, 520 ),
(507, 11, 521 ),
(508, 11, 522 ),
(509, 11, 523 ),
(510, 11, 524 ),
(511, 11, 525 ),
(512, 11, 526 ),
(513, 11, 527 ),
(514, 11, 528 ),
(515, 11, 529 ),
(516, 11, 221 ),
(517, 11, 531 ),
(518, 11, 532 ),
(519, 11, 533 ),
(520, 11, 534 ),
(521, 11, 535 ),
(522, 11, 536 ),
(523, 11, 537 ),
(524, 11, 538 ),
(525, 11, 539 ),
(526, 11, 540 ),
(527, 11, 541 ),
(528, 11, 474 ),
(529, 11, 543 ),
(530, 11, 544 ),
(531, 11, 545 ),
(532, 11, 546 ),
(533, 11, 547 ),
(534, 11, 548 ),
(535, 11, 549 ),
(536, 11, 550 ),
(537, 11, 551 ),
(538, 11, 552 ),
(539, 11, 553 ),
(540, 11, 554 ),
(541, 11, 555 ),
(542, 11, 556 ),
(543, 11, 557 ),
(544, 11, 558 ),
(545, 11, 409 ),
(546, 11, 560 ),
(547, 11, 561 ),
(548, 11, 562 ),
(549, 11, 563 ),
(550, 11, 564 ),
(551, 11, 617 ),
(552, 11, 618 ),
(553, 11, 619 ),
(554, 11, 620 ),
(555, 11, 621 ),
(556, 11, 622 ),
(557, 11, 284 ),
(558, 11, 630 ),
(559, 11, 632 ),
(560, 11, 633 ),
(561, 11, 634 ),
(562, 11, 637 ),
(563, 11, 638 ),
(564, 11, 639 ),
(565, 11, 640 ),
(566, 11, 641 ),
(567, 11, 646 ),
(568, 11, 647 ),
(569, 11, 648 ),
(570, 11, 649 ),
(571, 11, 655 ),
(572, 11, 657 ),
(573, 11, 694 ),
(574, 11, 702 ),
(575, 11, 723 ),
(576, 11, 800 ),
(577, 12, 4 ),
(578, 12, 7 ),
(579, 12, 8 ),
(580, 12, 9 ),
(581, 12, 11 ),
(582, 12, 13 ),
(583, 12, 15 ),
(584, 12, 16 ),
(585, 12, 21 ),
(586, 12, 22 ),
(587, 12, 25 ),
(588, 12, 26 ),
(589, 12, 29 ),
(590, 12, 30 ),
(591, 12, 31 ),
(592, 12, 32 ),
(593, 12, 36 ),
(594, 12, 37 ),
(595, 12, 38 ),
(596, 12, 41 ),
(597, 12, 42 ),
(598, 12, 43 ),
(599, 12, 44 ),
(600, 12, 45 ),
(601, 12, 46 ),
(602, 12, 47 ),
(603, 12, 48 ),
(604, 12, 49 ),
(605, 12, 50 ),
(606, 12, 51 ),
(607, 12, 52 ),
(608, 12, 53 ),
(609, 12, 54 ),
(610, 12, 55 ),
(611, 12, 56 ),
(612, 12, 60 ),
(613, 12, 61 ),
(614, 12, 62 ),
(615, 12, 63 ),
(616, 12, 64 ),
(617, 12, 65 ),
(618, 12, 66 ),
(619, 12, 68 ),
(620, 12, 69 ),
(621, 12, 70 ),
(622, 12, 72 ),
(623, 12, 74 ),
(624, 12, 79 ),
(625, 12, 82 ),
(626, 12, 84 ),
(627, 12, 87 ),
(628, 12, 95 ),
(629, 12, 97 ),
(630, 12, 98 ),
(631, 12, 99 ),
(632, 12, 100 ),
(633, 12, 101 ),
(634, 12, 102 ),
(635, 12, 103 ),
(636, 12, 106 ),
(637, 12, 109 ),
(638, 12, 110 ),
(639, 12, 111 ),
(640, 12, 112 ),
(641, 12, 113 ),
(642, 12, 114 ),
(643, 12, 317 ),
(644, 12, 318 ),
(645, 12, 319 ),
(646, 12, 320 ),
(647, 12, 321 ),
(648, 12, 322 ),
(649, 12, 323 ),
(650, 12, 325 ),
(651, 12, 326 ),
(652, 12, 327 ),
(653, 12, 335 ),
(654, 12, 339 ),
(655, 12, 426 ),
(656, 12, 427 ),
(657, 12, 428 ),
(658, 12, 429 ),
(659, 12, 430 ),
(660, 12, 431 ),
(661, 12, 432 ),
(662, 12, 433 ),
(663, 12, 434 ),
(664, 12, 435 ),
-- (665, 12, 436 ),
(666, 12, 437 ),
-- (667, 12, 437 ),
(668, 12, 439 ),
(669, 12, 440 ),
(670, 12, 441 ),
(671, 12, 442 ),
(672, 12, 443 ),
(673, 12, 444 ),
(674, 12, 565 ),
(675, 12, 566 ),
(676, 12, 567 ),
(677, 12, 436 ),
(678, 12, 569 ),
(679, 12, 570 ),
(680, 12, 571 ),
(681, 12, 572 ),
(682, 12, 573 ),
(683, 12, 574 ),
(684, 12, 575 ),
(685, 12, 576 ),
(686, 12, 577 ),
(687, 12, 578 ),
(688, 12, 579 ),
(689, 12, 580 ),
(690, 12, 581 ),
(691, 12, 474 ),
(692, 12, 583 ),
(693, 12, 584 ),
(694, 12, 585 ),
(695, 12, 586 ),
(696, 12, 587 ),
(697, 12, 588 ),
(698, 12, 589 ),
(699, 12, 590 ),
(700, 12, 591 ),
(701, 12, 592 ),
(702, 12, 593 ),
(703, 12, 623 ),
(704, 12, 624 ),
(705, 12, 625 ),
(706, 12, 627 ),
(707, 12, 643 ),
(708, 12, 653 ),
(709, 12, 654 ),
(710, 12, 656 ),
(711, 12, 660 ),
(712, 12, 661 ),
(713, 12, 662 ),
(714, 12, 690 ),
(715, 12, 691 ),
(716, 12, 695 ),
(717, 12, 696 ),
(718, 12, 700 ),
-- (719, 12, 69 ),
(720, 12, 706 ),
(721, 12, 716 ),
(722, 12, 717 ),
(723, 12, 724 ),
(724, 12, 725 ),
(725, 12, 726 ),
(726, 12, 727 ),
(727, 12, 728 ),
(728, 12, 729 ),
-- (729, 12, 11 ),
(730, 12, 732 ),
(731, 12, 733 ),
(732, 12, 734 ),
(733, 12, 735 ),
(734, 12, 736 ),
(735, 12, 737 ),
(736, 12, 739 ),
-- (737, 12, 62 ),
(738, 12, 743 ),
(739, 12, 744 ),
(740, 12, 746 ),
(741, 12, 747 ),
(742, 12, 751 ),
(743, 12, 752 ),
(744, 12, 757 ),
(745, 12, 759 ),
(746, 12, 761 ),
(747, 12, 762 ),
(748, 12, 763 ),
(749, 12, 764 ),
(750, 12, 766 ),
(751, 12, 767 ),
(752, 12, 769 ),
(753, 12, 770 ),
(754, 12, 771 ),
(755, 12, 772 ),
(756, 12, 777 ),
(757, 12, 779 ),
(758, 12, 780 ),
-- (759, 12, 11 ),
(760, 12, 784 ),
(761, 12, 785 ),
(762, 12, 789 ),
(763, 12, 790 ),
(764, 12, 791 ),
(765, 12, 792 ),
(766, 12, 796 ),
(767, 12, 797 ),
(768, 12, 801 ),
(769, 12, 804 ),
(770, 12, 805 ),
(771, 12, 807 ),
(772, 12, 810 ),
(773, 12, 811 ),
(774, 12, 813 ),
(775, 13, 89 ),
(776, 13, 90 ),
(777, 13, 91 ),
(778, 13, 92 ),
(779, 13, 93 ),
(780, 13, 94 ),
(781, 13, 104 ),
(782, 13, 105 ),
(783, 13, 107 ),
(784, 13, 108 ),
-- (785, 13, 116 ),
(786, 13, 117 ),
(787, 13, 594 ),
(788, 13, 595 ),
(789, 13, 596 ),
(790, 13, 597 ),
(791, 13, 598 ),
(792, 13, 599 ),
(793, 13, 600 ),
(794, 13, 601 ),
(795, 13, 602 ),
(796, 13, 603 ),
(797, 13, 604 ),
(798, 13, 605 ),
(799, 13, 606 ),
(800, 13, 607 ),
(801, 13, 608 ),
(802, 13, 609 ),
(803, 13, 610 ),
(804, 13, 611 ),
(805, 13, 612 ),
(806, 13, 12 ),
(807, 13, 614 ),
(808, 13, 629 ),
(809, 13, 658 ),
(810, 13, 116 ),
(811, 13, 705 ),
(812, 13, 714 ),
(813, 13, 808 )"""
    cursor = connection.cursor()
    cursor.execute(postgreSql_insert_query)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into Type_Desc table")
    cursor.close()
except psycopg2.OperationalError as error:
    print("Failed to insert record into Type_Desc table {}".format(error))