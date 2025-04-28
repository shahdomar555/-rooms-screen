import 'package:flutter/material.dart';
import '../models/room.dart';
import 'device_widget.dart';

class RoomCard extends StatelessWidget {
  final Room room;

  const RoomCard({super.key, required this.room});

  @override
  Widget build(BuildContext context) {
    return Card(
      margin: const EdgeInsets.only(bottom: 16),
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(16),
      ),
      clipBehavior: Clip.antiAlias,
      child: Stack(
        children: [
          // صورة الغرفة (من الأصول المحلية assets)
          Image.asset(
            room.imageUrl, // هنا بستخدم Asset بدل Network
            height: 180,
            width: double.infinity,
            fit: BoxFit.cover,
          ),
          // لون شفاف فوق الصورة
          Container(
            height: 180,
            decoration: BoxDecoration(
              color: Colors.black.withOpacity(0.3),
            ),
          ),
          // اسم الغرفة والمعلومات
          Positioned(
            top: 16,
            left: 16,
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  room.name,
                  style: const TextStyle(
                    color: Colors.white,
                    fontSize: 20,
                    fontWeight: FontWeight.bold,
                  ),
                ),
                const SizedBox(height: 8),
                Text(
                  '${room.activeDevices}/${room.totalDevices} is on',
                  style: const TextStyle(
                    color: Colors.white70,
                    fontSize: 14,
                  ),
                ),
              ],
            ),
          ),
          // أجهزة تحت
          Positioned(
            bottom: 16,
            left: 16,
            child: Row(
              children: const [
                DeviceWidget(icon: Icons.tv),
                DeviceWidget(icon: Icons.router),
                DeviceWidget(icon: Icons.lightbulb),
              ],
            ),
          )
        ],
      ),
    );
  }
}

